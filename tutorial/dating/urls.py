from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('home/', views.home, name='主页'),
    path('attention/', views.attention, name='关注者'),
    path('invitees/', views.invitation, name='邀请人员'),
    path('profile/', views.profile, name='修改'),
    path('accounts/login/', auth_views.login, name='登录'),
    path('accounts/logout/', auth_views.logout, kwargs={'next_page': '/'}, name='登出'),
    path('', views.index, name='index'),
]
