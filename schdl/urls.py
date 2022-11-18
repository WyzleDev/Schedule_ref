from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webview/', include('webview.urls')),
    path('api/', include('api.urls'))
]
