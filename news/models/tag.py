from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    created = models.DateTimeField(auto_now=True)
    updared = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'news'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
