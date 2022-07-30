from django.db import models


class LessonType(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Тип занятия', default='Лекция')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
        verbose_name = 'Тип занятия'
        verbose_name_plural = 'Типы занятий'
