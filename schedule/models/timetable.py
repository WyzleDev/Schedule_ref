from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _


class Timetable(models.Model):
    time_from = models.TimeField(_("с:"))
    time_to = models.TimeField(_("до:"))

    def __str__(self) -> str:
        return f'{self.time_from}-{self.time_to}'

    class Meta:
        verbose_name = _("Время с-до")
        verbose_name_plural = _("Времена с-до")
        app_label = 'api'
