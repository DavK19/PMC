from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, EventoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
