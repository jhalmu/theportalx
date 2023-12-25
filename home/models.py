from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser


class About_page(models.Model):
    title = models.CharField(_('Mood'), max_length=100)
    content = models.TextField(_('About'))
    date_posted = models.DateTimeField(_('Published'), default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('about')
        verbose_name_plural = _('abouts')

    def __str__(self):
        return self.title
