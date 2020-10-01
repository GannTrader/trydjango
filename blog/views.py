from django.views.generic import ListView, DetailView

from blog.models import PostModel


class PostListView(ListView):
    model = PostModel
    template_name = "blog/posts.html"


class PostDetailView(DetailView):
    model = PostModel
    template_name = "blog/post.html"
