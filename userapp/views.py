from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserModel
def loginview(request):
    return render(request,'userapp/login.html')

def registerview(request):
    if request.method=="POST":
        fname =request.POST.get("Firstname")
        lname =request.POST.get("Lastname")
        username =request.POST.get("Username")
        emailaddress =request.POST.get("Email address")
        password=request.POST.get("Password")
        confirmpassword=request.POST.get("Confirm Password")
        status=request.POST.get("Status")
        profilepicture=request.POST.get("Profile Picture")

        user=User(username=username, password=password, first_name=fname, last_name=lname, email=emailaddress, is_active=True)
        user.save()
        usermodel=UserModel(auth=user, status=status, profilepicture=profilepicture)
        usermodel.save()
        return redirect('index')
    else:
        return render(request,'userapp/register.html')


