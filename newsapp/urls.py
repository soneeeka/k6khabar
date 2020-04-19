from django.urls import path
from django.contrib import admin

from .views import index, detail, categorynews,add_postview,deletepost,editpost,search,comment_view,deletecomment,editcomment

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('topic/<int:id>/', categorynews, name='topic'),
    path('add_post/', add_postview,name="add_postview"),
    path('delete/<int:id>/',deletepost, name="deletepost"),
    path('edit/<int:id>/',editpost, name='editpost'),
    path('comment/<int:id>/',comment_view,name='comment'),
    path('deletecomment/<int:id>/',deletecomment,name='deletecomment'),
    path('editcomment/<int:id>/',editcomment,name='editcomment'),
    path('search/',search, name='search'),
    
]
