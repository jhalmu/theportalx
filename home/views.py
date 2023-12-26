from django.shortcuts import render

from .models import About_page


def home_view(request):
    return render(request, "home_index.html", {})

def contact_view(request):
    return render(request, "home_contacts.html", {})


def about_view(request):
    context = {"abouts": About_page.objects.all()}
    return render(request, "home_about.html", context)
