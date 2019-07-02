from django.db import models

# Create your models here.
class Usuario(models.Model):
    """ Define la tabla Usuario """
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80)
    email = models.EmailField (blank=True, unique=True)
    direccion = models.CharField(max_length=256, null=True, blank=True)