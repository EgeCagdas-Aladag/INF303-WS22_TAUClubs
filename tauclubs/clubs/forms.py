from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    model= Post
    fields= ['name','clubname', 'description']