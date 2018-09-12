from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=150)
    user = get_user_model()
    
    def __str__(self):
        return self.user