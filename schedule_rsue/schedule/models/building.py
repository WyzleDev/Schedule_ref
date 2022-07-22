from django.db import models
from django.utils.translation import gettext_lazy as _


class Building(models.Model):
    corpus = models.CharField(
        _('корпус'),
        max_length=40,
        default='Главный корпус',
    )
    address = models.CharField(
        _('адрес'),
        max_length=120,
        default='Дубининская ул., 25',
    )

    def __str__(self):
        return f'{self.corpus}, {self.address}'

    class Meta:
        app_label = 'api'
