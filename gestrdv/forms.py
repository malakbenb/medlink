from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['date_heure', 'motif']
        widgets = {
            'date_heure': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'motif': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }