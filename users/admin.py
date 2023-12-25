from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "full_name",
        "is_staff",
        "is_active",
        "email",
        
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
        "nick_name",
    )
    fieldsets = (
        (
            None,
            {"fields": ("email", "password", "nick_name", "first_name", "last_name")},
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            _("Name"),
            {
                "classes": ("wide",),
                "fields": (
                    "nick_name",
                    "first_name",
                    "last_name",
                    "email",
                ),
            },
        ),
        (
            _("Password"),
            {
                "classes": ("wide",),
                "fields": (
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            _("Rights"),
            {
                "classes": ("wide",),
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
