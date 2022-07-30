from django.db import models


class Auditory(models.Model):
    number = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Номер аудитории')
    building = models.ForeignKey(
        'api.Building', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Здание')

    def __str__(self):
        return f'{self.number}'

    class Meta:
        app_label = 'api'
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'
