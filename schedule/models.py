import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.


class Year(models.Model):
    date = models.CharField(max_length=30, null=False, default=f"{datetime.datetime.now().year}",
                            verbose_name='Заголовок', unique=True)

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'Расписание на год'
        verbose_name_plural = 'Расписания на года'


class Week(models.Model):
    title = models.IntegerField(null=False, default=1, verbose_name='Номер недели', unique=True)
    year = models.ForeignKey(Year, verbose_name='год', on_delete=models.CASCADE, to_field='date')
    is_even = models.BooleanField(verbose_name="Четная/нечетная", default=False)

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
    day_choice = models.TextChoices('week_days', "Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье")
    week_day = models.CharField(max_length=30, null=False, choices=day_choice.choices, default=day_choice.choices[0])

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
    surname = models.CharField(max_length=32, null=True, blank=True, verbose_name="фамилия")
    name = models.CharField(max_length=32, null=True, blank=True, verbose_name="имя")
    patronym = models.CharField(max_length=32, null=True, blank=True, verbose_name="Отчество")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    building = models.ForeignKey(Building, verbose_name='Корпус', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronym}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Group(models.Model):
    abbreviation_on_ru = models.CharField(max_length=5, unique=True, verbose_name="Аббревиатура на русском")
    abbreviation_on_eng = models.CharField(max_length=5, unique=True, verbose_name="Аббревиатура на английском")
    tutor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='Куратор')

    def __str__(self):
        return f'{self.abbreviation_on_ru}'


class Lesson(models.Model):
    title = models.CharField(max_length=30, null=False, default=1, verbose_name='название пары', unique=True)
    week = models.ForeignKey(Week, on_delete=models.CASCADE, verbose_name="неделя", null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name='день недели', null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='Учитель', null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Корпус', null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа", null=True)

    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.week} | {self.day}'

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


class TimeTable(models.Model):
    time_from = models.TimeField(verbose_name='Время начала')
    time_to = models.TimeField(verbose_name='Время окончания')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Расписание', null=True)

    def __str__(self):
        return f'{self.lesson} | {self.time_from}-{self.time_to}'

    class Meta:
        verbose_name = 'Время пары'
        verbose_name_plural = 'Времена пар'

# @receiver(pre_save, sender=Week)
# def check_is_even_week(sender, instance, *args, **kwargs):
#     if instance.