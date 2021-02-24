from django.db import models

# Create your models here.
class subscriber(models.Model):
    email=models.CharField(max_length=42)
    name=models.TextField()

    def __str__(self):
        return self.email