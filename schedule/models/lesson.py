from django.db import models
from django.utils.translation import gettext_lazy as _


class Lesson(models.Model):
    lesson_name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Название пары')
    group = models.ForeignKey("api.Group", on_delete=models.CASCADE,
                              null=False, blank=False, verbose_name="Группа")
    auditory = models.ForeignKey(
        'api.Auditory', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Аудитория')
    professor = models.ForeignKey(
        'api.Professor', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Преподаватель')
    time_table = models.ForeignKey(
        'api.Timetable', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Время')
    lesson_type = models.ForeignKey("api.LessonType", on_delete=models.CASCADE,
                                    null=False, blank=False, verbose_name="Тип занятия")
    even_week = models.BooleanField(
        verbose_name='Четная/нечетная неделя', null=False, blank=False)

    DAYS = (
        (1, _('Понедельник')),
        (2, _('Вторник')),
        (3, _('Среда')),
        (4, _('Четверг')),
        (5, _('Пятница')),
        (6, _('Суббота')),
        (7, _('Воскресенье')),
    )
    day = models.IntegerField(
        _('день недели'),
        choices=DAYS,
    )

    def __str__(self):
        return f'{self.lesson_name}, {self.group}, {self.day}'

    class Meta:
        app_label = 'api'
        ordering = ['day']
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'
