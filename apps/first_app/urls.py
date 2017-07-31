"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from .models import User

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success, name='success'),
    url(r'^home$', views.success, name='success'),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add-friend/(?P<id>\d+)$', views.addFriend),
    url(r'^remove-friend/(?P<id>\d+)$', views.removeFriend),
    url(r'^view-profile/(?P<id>\d+)$', views.viewProfile),
    url(r'^view-friendprofile/(?P<id>\d+)$', views.viewfriendProfile),
]
