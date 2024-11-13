from django.contrib import admin
from .models import Evento

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'ubicacion')
    search_fields = ('nombre', 'ubicacion')