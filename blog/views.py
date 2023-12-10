from django.shortcuts import render

# from .models import Blog_page


def blog_view(request):
    return render(request, "blog/index.html", {})


# def about_view(request):
#    context = {"abouts": About_page.objects.all()}
#    return render(request, "home/about.html", context)
#    return render(request, "home/about.html", context)
