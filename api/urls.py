"""BTP_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from api.views import *
from .views.check_tags import check_tags
from .views.upload_file import upload_file
from .views.ping import ping
from .views.login_view import login_view
from .views.register_view import register_view
from .views.download import download_file



urlpatterns = [
    path('check_tags/', check_tags, name='check_tags'),
    path('upload/', upload_file, name='upload_file'),
    path('download/', download_file, name='download_file'),
    path('ping/', ping, name='ping'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
