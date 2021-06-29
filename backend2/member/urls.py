from django.urls import path, include
# from .views import SignupAPI
from .views import HelloAPI, RegistrationAPI, MemberCreate
from . import views
from .views import Connection

urlpatterns = [
    # path('hello/', Connection.as_view()),
    path('hello/', views.HelloAPI),
    # path('signup/', views.Auth.as_view()),
    path('signup/', views.member_list)
]