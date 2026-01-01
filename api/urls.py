from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'medecins', views.MedecinViewSet)
router.register(r'rendezvous', views.RendezVousViewSet)

urlpatterns = [
    path('', include(router.urls)),
]