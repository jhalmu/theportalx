from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionMixin,
)
from django.db import models
from django.db.models import F
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        pass


class CustomUser(AbstractBaseUser, PermissionMixin):
    email = models.EmailField(_("email adderess"), unique=True)
    user_name = models.CharField(_("Username"), max_length=150, unique=True)
    first_name = models.CharField(_("First Name"), max_length=50, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=100, blank=True)
    full_name = models.GeneratedField(
        expression=F("first_name") + " " + F("last_name"),
        output_field=models.CharField(),
        db_persist=True,
        blank=True,
    )
    start_date = models.DateField(_("Start Date"), default=timezone.now)
    about = models.TextField(_("About"), max_lenght=500, blank=True)
    is_staff = models.BooleanField(_("Staff?"), default=False)
    is_active = models.BooleanField(_("Active"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    def __str__(self):
        return self.user_name
