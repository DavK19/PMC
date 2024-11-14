from django.db import models

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    eventos = models.ManyToManyField('Evento', related_name='usuarios_set')

    def __str__(self):
        return self.nombre

from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    latitud = models.FloatField(default=4.6014026)
    longitud = models.FloatField(default=-74.0660152)
    calificacion = models.FloatField(default=0.0)
    imagen = models.ImageField(upload_to='eventos', null=True, blank=True)
    usuarios = models.ManyToManyField('Usuario', related_name='eventos_set')

    def __str__(self):
        return self.nombre
