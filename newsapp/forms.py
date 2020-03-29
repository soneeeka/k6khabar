from django.forms import ModelForm
from .models import PostModel
class AddPostForm(ModelForm):#makepostform for easier
    class Meta:
        model=PostModel
        fields=['title','content','header_image','category']
        

