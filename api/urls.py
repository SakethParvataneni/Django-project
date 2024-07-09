# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ingest/', views.ingest_url, name='ingest_url'),
    path('urls/', views.get_urls, name='get_urls'),
]
