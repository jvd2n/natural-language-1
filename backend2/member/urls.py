from django.urls import path
from django.conf.urls import url, include
# from .views import SignupAPI
from .views_cbv import HelloAPI
from . import views_cbv
# from .views import Connection
# from .views import members as v_members, member as v_member
from .views_cbv import Members as members, MemberLogin as login
from rest_framework.urlpatterns import format_suffix_patterns

from member import views

urlpatterns = [
    url(r'^register/', views.members),
    url(r'^list/', views.members),
    url(r'^login/', views.member)
]

# urlpatterns = [
#     # path('hello/', Connection.as_view()),
#     path('hello/', views_cbv.HelloAPI),
#     # path('signup/', views.Auth.as_view()),
#     # path('signup/', views.member_list),
#     # url('register/', members.as_view()),
#     # path('login/<str:pk>/', login.as_view()),
#     # path('login/', login.as_view())
#     url(r'^register/', members.as_view()),
#     # path('<int:pk>/', v_member.as_view()),
#     url(r'^login/', v_member)
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
