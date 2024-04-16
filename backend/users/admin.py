from django.contrib import admin
from .models import profile
from .models import customer
from .models import business

# Register your models here.

admin.site.register(profile)
admin.site.register(customer)
admin.site.register(business)