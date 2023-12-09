from django.shortcuts import render

from .models import About_page


def home_view(request):
    return render(request, "home/index.html", {})


def about_view(request):
    context = {"abouts": About_page.objects.all()}
    return render(request, "home/about.html", context)
