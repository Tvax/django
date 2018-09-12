from django import forms

from .models import Post, Users

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'password',)
