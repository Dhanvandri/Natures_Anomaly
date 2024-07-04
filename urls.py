# anomaly/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('detect_anomaly/',views.detect_anomaly,name='detect_anomaly'),
]
