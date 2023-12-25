from django.views import generic 
#import ListView, DetailView
from django.shortcuts import render

from .models import Post


# def blog_view(request):
#    context = {
#        "posts": Post.objects.all()
#        }
#    return render(request, "blog/index.html", context)

class PostList(generic.ListView):
    queryset = Post.objects.filter(published=True).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'