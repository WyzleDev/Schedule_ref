from django.contrib import admin


from django_admin_geomap import ModelAdmin
from .models import *


# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_filter = ['week', 'day']

    class Meta:
        model = Lesson


class EventAdmin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "37.9"
    geomap_default_latitude = "55.739"
    geomap_default_zoom = "10.2"
    geomap_item_zoom = "18"


admin.site.register(Event, EventAdmin)
admin.site.register(Tag)
admin.site.register(Week)
admin.site.register(Year)
admin.site.register(Day)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Building)
admin.site.register(Professor)
admin.site.register(TimeTable)
admin.site.register(Group)
