from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)
    calificacion = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre
