"""firstproj URL Configuration

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

from myapp.views import hello, hello1, hello2, students
#從student裡面的views抓取資料 
from students.views import listone, listall, post, post1, postform, delete, edit
#TEMPLATE加這裡就要加
#                                       別名
from CookieSessionApp import views as csviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('hello/', hello),
    path('hello1/<str:username>/', hello1),
    path('hello2/<str:username>/', hello2),
    path('stds/', students),
    path('listone/', listone),
	path('listall/', listall),
    path('post/', post),
    path('post1/', post1),
    path('postform/', postform),
    path('delete/<str:stdID>/', delete),
    path('edit/<str:stdID>/', edit),
    path('edit/<str:stdID>/<str:mode>/', edit),
]
