from rest_framework import viewsets
from gestrdv.models import Medecin, RendezVous
from .serializers import MedecinSerializer, RendezVousSerializer

class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class RendezVousViewSet(viewsets.ModelViewSet):
    queryset = RendezVous.objects.all()
    serializer_class = RendezVousSerializer