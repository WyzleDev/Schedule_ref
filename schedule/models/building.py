from django.db import models


class Building(models.Model):
    corpus = models.CharField(
        max_length=100, null=False, blank=False, default='Главный корпус', verbose_name='Корпус')
    address = models.CharField(
        max_length=100, null=False, blank=False, default="Дубининская улица, дом 25", verbose_name='Адрес')

    def __str__(self):
        return f'{self.corpus}, {self.address}'

    class Meta:
        app_label = 'api'
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
