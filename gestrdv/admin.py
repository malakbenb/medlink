from django.contrib import admin

# Register your models here.

from .models import Specialite, Medecin, RendezVous

admin.site.register(Specialite)
admin.site.register(Medecin)
admin.site.register(RendezVous)