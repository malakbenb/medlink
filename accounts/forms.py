from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InscriptionForm(UserCreationForm):
    first_name = forms.CharField(label="Prénom", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    # Pour sauvegarder le prénom/nom/email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user