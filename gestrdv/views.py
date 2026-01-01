

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Medecin
from .forms import RendezVousForm

@login_required(login_url='/admin/') # Redirige vers l'admin si pas connecté (pour faire simple)
def prendre_rdv(request, medecin_id):
    medecin = get_object_or_404(Medecin, id=medecin_id)
    
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rdv = form.save(commit=False)
            rdv.patient = request.user
            rdv.medecin = medecin
            rdv.save()
            return redirect('index') # Retour à l'accueil après validation
    else:
        form = RendezVousForm()
    
    return render(request, 'gestrdv/prendre_rdv.html', {'form': form, 'medecin': medecin})