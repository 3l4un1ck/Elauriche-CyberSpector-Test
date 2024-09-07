from django.contrib import admin
from .models import CSIRT

# Register your models here.
admin.site.register(CSIRT, admin.ModelAdmin)
