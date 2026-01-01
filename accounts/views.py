

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm
from gestrdv.models import RendezVous # On importe le modèle RDV de l'autre app

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Connecte l'utilisateur direct après inscription
            return redirect('dashboard')
    else:
        form = InscriptionForm()
    return render(request, 'accounts/inscription.html', {'form': form})

@login_required # Il faut être connecté pour voir ça
def dashboard(request):
    # Récupérer les RDV de l'utilisateur connecté
    mes_rdv = RendezVous.objects.filter(patient=request.user).order_by('-date_heure')
    
    return render(request, 'accounts/dashboard.html', {'mes_rdv': mes_rdv})