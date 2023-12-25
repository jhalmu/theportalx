from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), unique=True)
    first_name = models.CharField(_("First Name"), max_length=50, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=100, blank=True)
    full_name = models.GeneratedField(
        expression=Concat(
            "first_name",
            V(" "),
            "last_name",
        ),
        output_field=models.CharField(max_length=150, verbose_name=_("Full Name")),
        db_persist=True,
    )
    nick_name = models.CharField(_("Nick Name"), max_length=40, blank=True)
    start_date = models.DateField(_("Start Date"), default=timezone.now)
    about = models.TextField(_("About"), blank=True)
    is_staff = models.BooleanField(_("Staff?"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nick_name", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['is_active', 'is_staff']

    def __str__(self):
        return self.email
