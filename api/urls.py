from django.urls import path, include

from .views import LessonViewSet

urlpatterns = [
    path('v1/lessons/<str:group>/', LessonViewSet.as_view(), name='Lessons')
]
