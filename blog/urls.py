from django.urls import path

from . import views

urlpatterns = [
    path("", views.blog_view, name="blog"),
    # path("about", views.about_view, name="about"),
]
