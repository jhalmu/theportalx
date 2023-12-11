from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "body",
    )
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
