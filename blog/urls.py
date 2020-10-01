from django.urls import path

from blog.views import PostListView, PostDetailView, GetPostLike, SearchView, CommentView, PostByCategory

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post'),
    path('like/<slug:slug>', GetPostLike.as_view(), name='like'),
    path('search/', SearchView.as_view(), name='search'),
    path('comment/<slug:slug>', CommentView.as_view(), name='comment'),
    path('category/<slug:slug>', PostByCategory.as_view(), name='post_category'),
]