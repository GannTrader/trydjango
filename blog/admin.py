from django.contrib import admin

from blog.models import PostModel, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created_at", "category"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "created_at", "user", "status"]
    list_filter = ["created_at", "user", "status"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

admin.site.register(PostModel, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)