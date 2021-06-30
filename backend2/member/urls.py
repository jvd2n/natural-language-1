from django.urls import path, include
from django.conf.urls import url
# from .views import SignupAPI
from .views import HelloAPI
from . import views
# from .views import Connection
from .views import Members as members, MemberLogin as login
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('hello/', Connection.as_view()),
    path('hello/', views.HelloAPI),
    # path('signup/', views.Auth.as_view()),
    # path('signup/', views.member_list),
    url('signup/', members.as_view()),
    # path('login/<str:pk>/', login.as_view()),
    path('login/', login.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
