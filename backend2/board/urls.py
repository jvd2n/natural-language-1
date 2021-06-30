from django.urls import path, include
from django.conf.urls import url
from .views import Posts as posts

urlpatterns = [
    url('register/', posts.as_view())
]