from django.contrib import admin
from .models import Evento

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'latitud', 'longitud')  # Usar los campos correctos
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha',)