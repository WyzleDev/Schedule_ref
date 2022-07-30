from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name='Имя')
    surname = models.CharField(
        max_length=100, null=False, blank=False, verbose_name='Фамилия')
    patronymic = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Отчество")
    position = models.ForeignKey(
        "api.Position", on_delete=models.CASCADE, null=False, blank=False, verbose_name="Должность")
    email = models.EmailField(null=False, blank=False,
                              verbose_name="Электронная почта")
    phone = models.CharField(max_length=100, null=False,
                             blank=False, verbose_name="Телефон")
    building = models.ForeignKey(
        'api.Building', on_delete=models.CASCADE, null=False, blank=False, verbose_name="Здание")
    auditory = models.ForeignKey(
        'api.Auditory', on_delete=models.CASCADE, null=False, blank=False, verbose_name="Аудитория")

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'

    class Meta:
        app_label = 'api'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
