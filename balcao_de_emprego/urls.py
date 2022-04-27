from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vagas.urls')),
    path('admin/', admin.site.urls),
    path('c/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
