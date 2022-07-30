from django.db import models


class LessonName(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Название пары')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
        verbose_name = 'Название пары'
        verbose_name_plural = 'Названия пар'
