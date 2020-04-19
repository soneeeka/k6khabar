from django.forms import ModelForm
from .models import PostModel,CommentModel
class AddPostForm(ModelForm):#makepostform for easier
    class Meta:
        model=PostModel
        fields=['title','content','header_image','category']

class CommentForm(ModelForm):
    class Meta:
        model=CommentModel
        fields=['content','parent_post']
        

