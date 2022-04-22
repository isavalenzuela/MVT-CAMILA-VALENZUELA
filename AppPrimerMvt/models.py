from django.db import models

# Create your models here.
class Familia(models.Model):

    nombre_completo = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
