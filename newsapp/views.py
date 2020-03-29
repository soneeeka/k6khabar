from django.shortcuts import render, redirect
import datetime
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import PostModel, CategoryModel
from userapp.models import UserModel
from django.contrib.auth.models import User
import random
def index(request):
    posts = PostModel.objects.all().order_by()
    categories = CategoryModel.objects.all()[:5]
    num_of_post = len(posts)
    featured_post_index=random.randint(0,num_of_post-1)
    context = {
        'posts' : posts,
        'categories': categories,
        'featured_post': posts[featured_post_index] if len(posts) > 0 else None

    }
    return render(request, 'newsapp/index.html', context)

def detail(request, id):
    post = PostModel.objects.filter(id=id).first()
    categories = CategoryModel.objects.all()[:5]
    context = {
        'post': post,
        'categories': categories
    }
    return render(request, 'newsapp/detail.html', context)

def categorynews(request, id):
    category = CategoryModel.objects.filter(id=id).first()
    if category:
        posts = PostModel.objects.filter(category=category)
        categories = CategoryModel.objects.all()[:5]
        num_of_post = len(posts)
        featured_post_index=random.randint(0,num_of_post-1)
        context = {
            'posts': posts,
            'categories': categories,
            'featured_post' : posts[featured_post_index] if len(posts) > 0 else None,
            'current_category_id' :id
        }
        return render(request, 'newsapp/index.html', context)
    else:
        return render(request, 'newsapp/error404.html')
@login_required
def add_postview(request):
    if request.method=='POST':
        form=AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #now add logic to add form
            post= form.save(commit=False)
            django_user=User.objects.filter(id=request.user.id).first()
            current_user=UserModel.objects.filter(auth=django_user).first()
            post.posted_by=current_user
            post.save()
            return redirect('index')
        else:
            return render(request,'newsapp/add_post.html',{'form':form})

    else:
        form=AddPostForm()

        categories=CategoryModel.objects.all()[:5]
        context={
            'categories': categories,
            'form':form
        }
        return render(request,'newsapp/add_post.html',context)

@login_required
def deletepost(request,id):
    post=PostModel.objects.filter(id=id).first()
    if post:
        logged_in_user_id= request.user.id
        post_user_id=post.posted_by.auth.id
        if logged_in_user_id==post_user_id:
            post.delete()
            return redirect ('index')
        else:
            return render(request,'newsapp/error40.html') 

    
    else:
        #there is no page with that id
        return render(request, 'newsapp/error404.html')

@login_required
def editpost(request,id):
    if request.method=='POST':
        
        form=AddPostForm(request.POST, request.FILES)
        post=PostModel.objects.filter(id=id).first()
        if post:
            current_user_id=request.user.id
            post_user_id= post.posted_by.auth.id
            if current_user_id==post_user_id:
                form=AddPostForm(request.POST, files=request.FILES, instance=post)
                if form.is_valid():
                    form.save()
                    return redirect('detail', post.id)
                else:
                    return render(request, 'newsapp/editpost.html', {'form':form})

            
            else:
                return render(request,'newsapp/error404.html')
    else:
        post=PostModel.objects.filter(id=id).first()
        if post:
            form=AddPostForm(instance=post)
            return render(request,'newsapp/edit_post.html',{'form':form})
        else:
            return render(request, 'newsapp/error404.html')

def search(request):
    categories=CategoryModel.objects.all()[:5]
    query=request.GET.get('query')
    result_in_title=PostModel.objects.filter(title__icontains = query)
    result_in_content=PostModel.objects.filter(content__icontains = query)
    result=(result_in_title | result_in_content).distinct()
    context={
        'posts':result,
        'search_query':query,
        'categories':categories
    }
    return render(request, 'newsapp/search_result.html',context)