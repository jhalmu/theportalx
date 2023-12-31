from django.views.generic import DetailView, ListView

from .models import Post

# def blog_view(request):
#    context = {
#        "posts": Post.objects.all()
#        }
#    return render(request, "blog/index.html", context)


class PostList(ListView):
    queryset = Post.objects.filter(published=True).order_by("-created_on")
    template_name = "blog_index.html"


class PostDetail(DetailView):
    model = Post
    template_name = "blog_detail.html"
