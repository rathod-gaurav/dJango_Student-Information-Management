from django.contrib import admin
from .models import JsonUpload, StudentProfile

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(JsonUpload)