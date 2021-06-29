from django.urls import path
from .views import SignupAPI
from . import views

urlpatterns = [
    path('member/signup', views.member_list),
]