from django.contrib import admin
from .models import *


# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_filter = ['week', 'day']

    class Meta:
        model = Lesson


admin.site.register(Week)
admin.site.register(Year)
admin.site.register(Day)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Building)
admin.site.register(Professor)
admin.site.register(TimeTable)
admin.site.register(Group)
