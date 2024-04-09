from django.db import models

# Create your models here.

class profile(models.Model):
    unique_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"ID: {self.unique_id},  Name: {self.name}, Email: {self.email}"


class customer (models.Model):
    profile_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255) 
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f" {self.profile_id} {self.name} {self.address} {self.city} {self.country}"

    def get_profile(self):
        return profile.objects.get(unique_id=self.profile_id)