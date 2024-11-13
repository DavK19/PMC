from rest_framework import serializers
from .models import Usuario, Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    # Para mostrar la información de los eventos a los que está inscrito el usuario
    eventos = EventoSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'contrasena', 'eventos']
        extra_kwargs = {'contrasena': {'write_only': True}}

class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'eventos']

    