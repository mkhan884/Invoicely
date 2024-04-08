from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.email} {self.password}"