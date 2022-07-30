from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
