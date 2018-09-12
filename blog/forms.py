from django import forms

from .models import Post, Users, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'password',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)