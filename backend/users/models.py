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
    profile_id = models.ForeignKey(profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) 
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f" {self.profile_id.unique_id} {self.name} {self.address} {self.city} {self.country} {self.phone_number}"

    def get_profile(self):
        return profile.objects.get(unique_id=self.profile_id)
    
class business(models.Model):
    profile_id = models.ForeignKey(profile, on_delete=models.CASCADE)
    business_unique_id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=255)
    business_phone_number = models.CharField(max_length=255)
    business_address = models.CharField(max_length=255)
    business_city = models.CharField(max_length=255)
    business_country = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    organization_type = models.CharField(max_length=255)

    def __str__(self):
        return f" {self.profile_id.unique_id} {self.business_unique_id} {self.business_name} {self.business_address} {self.business_city} {self.business_country} {self.business_phone_number} {self.organization_type}"