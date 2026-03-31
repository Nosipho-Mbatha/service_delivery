from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('service/', include('service_desk.urls')),
]