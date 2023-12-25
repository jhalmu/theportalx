from django.contrib import admin

from .models import Comment, Post, Category

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post","created_on",)
    list_filter = ["created_on","author", "post", ]

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "upload",
        "photo_url",
        "slug",
        "published",
        "created_on",
        "published_on",
        "last_modified",
    )
    list_filter = ("created_on","author","published","locale",)
    search_fields = ['title', 'body']
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    search_fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)