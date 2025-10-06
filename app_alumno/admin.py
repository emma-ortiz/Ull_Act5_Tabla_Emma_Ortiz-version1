from django.contrib import admin

# Register your models here.
from .models import Alumno 
# registrar el modelio Alumno en el admin 
admin.site.register(Alumno)
