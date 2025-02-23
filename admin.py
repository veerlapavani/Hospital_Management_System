from django.contrib import admin
from .models import Doctor,Department,Patient,Appointment

# Register your models here.
admin.site.register((Department,Doctor,Patient,Appointment))
