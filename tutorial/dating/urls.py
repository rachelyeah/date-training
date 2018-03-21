from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from registration.backends.simple import urls
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('home/', views.home, name='主页'),
    path('attention/', views.attention, name='关注者'),
    path('invitees/', views.invitation, name='邀请人员'),
    path('profile/', views.profile, name='修改'),
    path('upage/<int:member_id>/', views.upage, name='朋友主页'),
    # path('account/', include('registration.backends.simple.urls'), name='注册'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    path('accounts/login/', auth_views.login, name='登录'),
    path('accounts/logout/', auth_views.logout, kwargs={'next_page': '/'}, name='登出'),
    path('', views.index, name='index'),
    url(r'', include('django.contrib.auth.urls')),
]
