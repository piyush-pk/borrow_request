from django.contrib import admin
from .models import *
# Register your models here.

class adminRequest(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'device_price', 'time']

admin.site.register(Request, adminRequest)