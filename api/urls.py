from django.contrib import admin
from django.urls import path, include

from .views import LessonViewSet, NewsViewSet, ProfessorsViewSet, exactProfessorViewSet

urlpatterns = [
    path('v1/schedule/<int:even_week>/<str:group_name>/',
         LessonViewSet.as_view(), name='schedule'),
    path('v1/professor/<int:id>',
         exactProfessorViewSet.as_view(), name='professor'),
    path('v1/professors/', ProfessorsViewSet.as_view(), name='professors'),
    path('v1/news/', NewsViewSet.as_view(), name='news'),
]
