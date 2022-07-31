from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False,
                             null=False, verbose_name='Заголовок')
    text = models.TextField(blank=False, null=False, verbose_name='Текст')
    link_to_source = models.URLField(
        blank=False, null=False, verbose_name='Ссылка на источник')
    tags = models.ManyToManyField("news.Tag", related_name='posts')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        app_label = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
