from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import LessonViewSet,  EventsViewSet

urlpatterns = [
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('v1/lessons/<str:group>/', LessonViewSet.as_view(), name='Lessons'),
    path("v1/events/", EventsViewSet.as_view(), name="Events"),
]
