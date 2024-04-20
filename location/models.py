from django.db import models

from lib.common_models import BaseModel
from django.utils.translation import gettext_lazy as _


class Location(BaseModel):
    title = models.CharField(verbose_name=_('title'), max_length=32)
    points = models.JSONField(verbose_name=_('points'), )


    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")


    def __str__(self):
        return self.title