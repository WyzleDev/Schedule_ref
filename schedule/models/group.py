from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Название')
    specialization = models.ForeignKey(
        'api.Specialization', on_delete=models.CASCADE, null=False, blank=False, verbose_name="Специализация")
    abbriviation = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Аббривеатура')

    def __str__(self):
        return f'{self.name}, {self.specialization}'

    class Meta:
        app_label = 'api'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
