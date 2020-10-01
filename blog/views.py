from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from blog.models import PostModel, Comment, Category


class CategoryMixin(object):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class PostListView(CategoryMixin, ListView):
    queryset = PostModel.objects.all().order_by("-created_at")
    template_name = "blog/posts.html"


class PostDetailView(CategoryMixin, DetailView):
    model = PostModel
    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        _slug=self.kwargs["slug"]
        post = PostModel.objects.get(slug=_slug)
        total_likes = post.likes.count()
        liked = False
        if post.likes.filter(username=self.request.user).exists():
            liked = True
        context["liked"] = liked
        context["total_likes"] = total_likes

        comments = Comment.objects.filter(post=post, status="active")
        context["comments"] = comments
        return context


class GetPostLike(View):
    def get(self, *args, **kwargs):
        _slug = self.kwargs["slug"]
        post = PostModel.objects.get(slug=_slug)

        if post.likes.filter(username=self.request.user).exists():
            post.likes.remove(self.request.user)
        else:
            post.likes.add(self.request.user)
        return redirect(reverse_lazy("post", kwargs={"slug": _slug}))


class SearchView(View):
    def get(self, request):
        _keyword = request.GET["keyword"]
        posts = PostModel.objects.filter(title__contains=_keyword)
        total_results = posts.count()
        template_name = "blog/search_result.html"
        context = {"posts": posts, "total_results": total_results}
        return render(request, template_name, context)


class CommentView(View):
    def post(self, request, *args, **kwargs):
        _slug = self.kwargs["slug"]
        _post = PostModel.objects.get(slug=_slug)
        _comment = request.POST["comment"]

        Comment.objects.create(
            post = _post,
            user = request.user,
            text = _comment
        )
        return redirect(reverse_lazy("post", kwargs={"slug": _slug}))


class PostByCategory(View):
    def get(self, request, **kwargs):
        _slug = self.kwargs["slug"]
        _category = Category.objects.get(slug=_slug)
        posts = PostModel.objects.filter(category=_category)
        template_name = "blog/post_by_category.html"
        context = {"posts": posts}
        return render(request, template_name, context)