

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Liste des 58 Wilayas d'Algérie
WILAYAS_CHOICES = [
    ('Adrar', '01 - Adrar'),
    ('Chlef', '02 - Chlef'),
    ('Laghouat', '03 - Laghouat'),
    ('Oum El Bouaghi', '04 - Oum El Bouaghi'),
    ('Batna', '05 - Batna'),
    ('Béjaïa', '06 - Béjaïa'),
    ('Biskra', '07 - Biskra'),
    ('Béchar', '08 - Béchar'),
    ('Blida', '09 - Blida'),
    ('Bouira', '10 - Bouira'),
    ('Tamanrasset', '11 - Tamanrasset'),
    ('Tébessa', '12 - Tébessa'),
    ('Tlemcen', '13 - Tlemcen'),
    ('Tiaret', '14 - Tiaret'),
    ('Tizi Ouzou', '15 - Tizi Ouzou'),
    ('Alger', '16 - Alger'),
    ('Djelfa', '17 - Djelfa'),
    ('Jijel', '18 - Jijel'),
    ('Sétif', '19 - Sétif'),
    ('Saïda', '20 - Saïda'),
    ('Skikda', '21 - Skikda'),
    ('Sidi Bel Abbès', '22 - Sidi Bel Abbès'),
    ('Annaba', '23 - Annaba'),
    ('Guelma', '24 - Guelma'),
    ('Constantine', '25 - Constantine'),
    ('Médéa', '26 - Médéa'),
    ('Mostaganem', '27 - Mostaganem'),
    ('M\'Sila', '28 - M\'Sila'),
    ('Mascara', '29 - Mascara'),
    ('Ouargla', '30 - Ouargla'),
    ('Oran', '31 - Oran'),
    ('El Bayadh', '32 - El Bayadh'),
    ('Illizi', '33 - Illizi'),
    ('Bordj Bou Arreridj', '34 - Bordj Bou Arreridj'),
    ('Boumerdès', '35 - Boumerdès'),
    ('El Tarf', '36 - El Tarf'),
    ('Tindouf', '37 - Tindouf'),
    ('Tissemsilt', '38 - Tissemsilt'),
    ('El Oued', '39 - El Oued'),
    ('Khenchela', '40 - Khenchela'),
    ('Souk Ahras', '41 - Souk Ahras'),
    ('Tipaza', '42 - Tipaza'),
    ('Mila', '43 - Mila'),
    ('Aïn Defla', '44 - Aïn Defla'),
    ('Naâma', '45 - Naâma'),
    ('Aïn Témouchent', '46 - Aïn Témouchent'),
    ('Ghardaïa', '47 - Ghardaïa'),
    ('Relizane', '48 - Relizane'),
    ('Timimoun', '49 - Timimoun'),
    ('Bordj Badji Mokhtar', '50 - Bordj Badji Mokhtar'),
    ('Ouled Djellal', '51 - Ouled Djellal'),
    ('Béni Abbès', '52 - Béni Abbès'),
    ('In Salah', '53 - In Salah'),
    ('In Guezzam', '54 - In Guezzam'),
    ('Touggourt', '55 - Touggourt'),
    ('Djanet', '56 - Djanet'),
    ('El M\'Ghair', '57 - El M\'Ghair'),
    ('El Meniaa', '58 - El Meniaa'),
]


class Specialite(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Medecin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Pour lier à un compte utilisateur
    specialite = models.ForeignKey(Specialite, on_delete=models.SET_NULL, null=True)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=50, choices=WILAYAS_CHOICES, default='Alger')
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"Dr. {self.user.last_name} - {self.specialite}"

class RendezVous(models.Model):
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mes_rdv')
    date_heure = models.DateTimeField()
    motif = models.TextField()
    approuve = models.BooleanField(default=False)

    def __str__(self):
        return f"RDV le {self.date_heure} avec {self.medecin.user.last_name}"