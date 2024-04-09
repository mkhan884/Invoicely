from django.contrib import admin
from .models import profile
from .models import customer

# Register your models here.

admin.site.register(profile)
admin.site.register(customer)