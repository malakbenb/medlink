from django.urls import path
from . import views

urlpatterns = [
    path('nouveau/<int:medecin_id>/', views.prendre_rdv, name='prendre_rdv'),
    
]