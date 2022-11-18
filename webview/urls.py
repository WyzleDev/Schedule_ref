from django.urls import path

from . import views

urlpatterns = [
    path('<str:group>', views.IndexPage.as_view(), name='index')
]
