from rest_framework import serializers
from gestrdv.models import Medecin, RendezVous
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class MedecinSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Medecin
        fields = '__all__'

class RendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = RendezVous
        fields = '__all__'