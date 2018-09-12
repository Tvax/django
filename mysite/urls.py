from django.conf.urls import include, url
from django.contrib import admin

from django.contrib import auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]