from django.shortcuts import render

from .models import Post


def blog_view(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/index.html", context)


# def about_view(request):
#    context = {"abouts": About_page.objects.all()}
#    return render(request, "home/about.html", context)
#    return render(request, "home/about.html", context)
