from django.urls import path

from . import views

urlpatterns = [
    path("", views.stock_view, name="stock"),
    # path("about", views.about_view, name="about"),
]
