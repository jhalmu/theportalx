from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>', views.PostDetail.as_view(), name='blog_detail'),
]
