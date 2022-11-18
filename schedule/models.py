import datetime
from msilib.schema import Class
from time import timezone
from turtle import position
from xml.dom import ValidationErr

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_admin_geomap import GeoItem


class Year(models.Model):
    date = models.CharField(max_length=30, null=False, default=f"{datetime.datetime.now().year}",
                            verbose_name='Заголовок', unique=True)

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'Расписание на год'
        verbose_name_plural = 'Расписания на года'


class Week(models.Model):
    title = models.IntegerField(
        null=False, default=1, verbose_name='Номер недели')
    year = models.ForeignKey(Year, verbose_name='год',
                             on_delete=models.CASCADE, to_field='date')
    is_even = models.BooleanField(
        verbose_name="Четная/нечетная", default=False)

    def save(self):
        if self.title % 2 == 0:
            self.is_even = 1
        else:
            self.is_even = 0
        super(Week, self).save()

    def __str__(self):
        return f'Неделя {self.title}'

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'


class Day(models.Model):
    day_choice = models.TextChoices(
        'week_days', "Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье")
    week_day = models.CharField(
        max_length=30, null=False, choices=day_choice.choices, default=day_choice.choices[0])
    week = models.ForeignKey(
        Week, verbose_name='Неделя', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.week_day}'

    class Meta:
        verbose_name = 'день'
        verbose_name_plural = 'дни'


class Building(models.Model):
    address = models.CharField(max_length=128, verbose_name='Адрес')
    corp = models.CharField(max_length=64, default="Главное здание")

    def __str__(self):
        return f'{self.address} | {self.corp}'

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'


class Professor(models.Model):
    surname = models.CharField(
        max_length=32, null=True, blank=True, verbose_name="фамилия")
    name = models.CharField(max_length=32, null=True,
                            blank=True, verbose_name="имя")
    patronym = models.CharField(
        max_length=32, null=True, blank=True, verbose_name="Отчество")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    building = models.ForeignKey(
        Building, verbose_name='Корпус', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronym}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Group(models.Model):
    abbreviation_on_ru = models.CharField(
        max_length=5, unique=True, verbose_name="Аббревиатура на русском")
    abbreviation_on_eng = models.CharField(
        max_length=5, unique=True, verbose_name="Аббревиатура на английском")
    tutor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, verbose_name='Куратор')

    def __str__(self):
        return f'{self.abbreviation_on_ru}'

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class ScheduleElement(models.Model):
    name = models.CharField(
        max_length=128, verbose_name='Название', null=True, default="")
    starting_time = models.TimeField(
        verbose_name='Время начала', default='', editable=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Lesson(ScheduleElement):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, verbose_name='Преподаватель')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')
    pos_choices = models.TextChoices('position', "1 2 3 4 5")
    position = models.CharField(max_length=32, choices=pos_choices.choices,
                                default=pos_choices.choices[0], verbose_name='Номер пары')
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, verbose_name='День')
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, verbose_name='Корпус')
    room = models.CharField(max_length=5, verbose_name='Кабинет')
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, verbose_name='Преподаватель')

    def save(self, **kwargs):
        if self.professor.building != self.building:
            raise ValidationErr(
                'Преподаватель не работает в этом корпусе')
        if self.position == '1':
            self.starting_time = '08:30'
        elif self.position == '2':
            self.starting_time = '10:30'
        elif self.position == '3':
            self.starting_time = '12:10'
        elif self.position == '4':
            self.starting_time = '14:00'
        elif self.position == '5':
            self.starting_time = '15:40'
        super(Lesson, self).save()


class Tag(models.Model):
    title = models.CharField(max_length=64, null=False,
                             verbose_name="Название")

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Event(models.Model, GeoItem):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(
        max_length=256, verbose_name="Описание", default="", null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=_("Тэги"))
    time = models.TimeField(
        null=False, default="00:00", verbose_name="Начало")
    date = models.DateField(
        null=False, verbose_name="Дата")
    creator = models.CharField(
        max_length=128, null=False, blank=False, default="", verbose_name=_("Организатор"))

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Широта"))

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Долгота"))

    yandex_maps_url = models.URLField(
        null=True, blank=True, verbose_name="Ссылка на яндекс карты")

    def save(self):
        if self.yandex_maps_url == None or self.yandex_maps_url == '':
            self.yandex_maps_url = f'https://yandex.ru/maps/?pt={float(self.longitude)},{float(self.latitude)}&z=18&l=map'
        else:
            self.yandex_maps_url = self.yandex_maps_url
        super(Event, self).save()

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    @property
    def geomap_popup_view(self):
        return f"<strong>{self.title} - в {self.time}</strong> <br> {self.description} <br> {self.creator}"

    def __str__(self) -> str:
        return f'{self.title} | {self.time} | {self.creator}'

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
