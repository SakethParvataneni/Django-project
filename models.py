from django.db import models

class URL(models.Model):
    url = models.URLField()
    spidername = models.CharField(max_length=100)
    priority = models.IntegerField()
    metadata = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=50, default='pending')  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
