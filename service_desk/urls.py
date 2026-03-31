from django.urls import path
from .views import track_status

urlpatterns = [
    path('', track_status),
]