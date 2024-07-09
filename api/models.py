# api/models.py
from django.db import models

class URL(models.Model):
    url = models.URLField()
    spidername = models.CharField(max_length=100)  # E.g., NDTV, Eeenadu, etc.
    priority = models.IntegerField()
    metadata = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=50, default='pending')  # To track if URL is scraped or not

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
