from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField(blank=True, null=True)
#es para el administrador 
    def __str__(self):
        return f"{self.nombre} {self.email}"