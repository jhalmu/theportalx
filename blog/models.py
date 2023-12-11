from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Lower
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)


CHOICE = ((True, _("Yes")), (False, _("No")))

LOCALE = (
    ("FI", _("Finnish")),
    ("EN", _("English")),
    ("SV", _("Swedish")),
    ("ES", _("Spanish")),
)


class Post(models.Model):
    published = models.BooleanField(choices=CHOICE, default=True, blank=True)
    locale = models.CharField(choices=LOCALE, default="FI", blank="FI", max_length=5)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to="photos/% Y/% m/% d/")
    photo_url = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(
                Lower("title").desc(), "published_on", name="lower_title_date_idx"
            )
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
