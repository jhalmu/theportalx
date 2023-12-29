# from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Lower
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from users.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})


CHOICE = ((True, _("Yes")), (False, _("No")))

LOCALE = (
    ("FI", _("Finnish")),
    ("EN", _("English")),
    ("SV", _("Swedish")),
    ("ES", _("Spanish")),
)


class Post(models.Model):
    published = models.BooleanField(
        _("Published"), choices=CHOICE, default=True, blank=True
    )
    locale = models.CharField(
        _("Locale"), choices=LOCALE, default="FI", blank="FI", max_length=5
    )
    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), null=False, unique=True)
    body = models.TextField(_("Content"))
    created_on = models.DateTimeField(_("Created"), auto_now_add=True)
    published_on = models.DateTimeField(_("Publish date"), default=timezone.now)
    last_modified = models.DateTimeField(_("Last modified"), auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    upload = models.ImageField(
        _("Photo upload"), blank=True, upload_to="photos/%Y/%m/%d/"
    )
    photo_url = models.CharField(_("Photo Url"), blank=True, max_length=100)

    class Meta:
        indexes = [
            models.Index(
                Lower("title").desc(), "published_on", name="lower_title_date_idx"
            )
        ]
        verbose_name = _("blog post")
        verbose_name_plural = _("blog posts")

    def __str__(self):
        return self.title

    def number_of_posts(self):
        return Post.objects.count()

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author} on '{self.post}'"

    def number_of_comments(self):
        return self.comments.count()
