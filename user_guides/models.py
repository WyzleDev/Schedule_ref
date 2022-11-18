from django.db import models


class UserGuideTag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class UserGuide(models.Model):
    name = models.CharField(max_length=128, null=False,
                            blank=False, verbose_name="Название")
    description = models.TextField(
        null=False, blank=False, verbose_name="Описание")
    tags = models.ManyToManyField(UserGuideTag, verbose_name="Теги")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Руководство пользователя"
        verbose_name_plural = "Руководства пользователей"
