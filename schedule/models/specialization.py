from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Специальность')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'api'
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
