from django.contrib import admin

from .models import UserGuide, UserGuideTag


@admin.register(UserGuideTag)
class UserGuideTagAdmin(admin.ModelAdmin):
    model = UserGuideTag
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_editable = ['name', ]
    list_per_page = 20


@admin.register(UserGuide)
class UserGuideAdmin(admin.ModelAdmin):
    model = UserGuide

    list_display = ['id',   'name', 'description']
    list_filter = ['tags', ]
    search_fields = ['name', 'description']
    list_editable = ['description', ]
