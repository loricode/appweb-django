from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    celular = models.CharField(max_length=50)
