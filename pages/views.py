from django.shortcuts import render
from gestrdv.models import Medecin, Specialite, WILAYAS_CHOICES

# Mapping spécialité → nom de fichier (sans extension)
SPEC_IMAGES = {
    'Cardiologie': 'coeur',
    'Dermatologie': 'peau',
    'Pédiatrie': 'bebe',
    'Ophtalmologie': 'oeil',
    'Neurologie': 'cerveau',
    'Gastro-entérologie': 'estomac',
    'Pneumologie': 'poumon',
    'Endocrinologie': 'hormone',
    'Généraliste': 'generaliste',
    'Oncologie': 'cancer',
    'Radiologie': 'radio',
    'Chirurgie générale': 'chirurgie',
    'Orthopédie': 'os',
    'Urologie': 'rein',
    'Gynécologie': 'uterus',
    'Obstétrique': 'bebe',
    'Psychiatrie': 'cerveau',
    'Rhumatologie': 'main',
    'Oto-rhino-laryngologie': 'oreille',
    'Anesthésiologie': 'seringue',
    'Hématologie': 'sang',
    'Néphrologie': 'rein',
    'Immunologie': 'defense',
    ' infectieuse': 'virus',
    'Dentiste': 'dent',
    'Stomatologie': 'dent',
    'Chirurgie maxillo-faciale': 'dent',
    'Allergologie': 'pollen',
    'Kinésithérapie': 'epaule',
    'Médecine du sport': 'sport',
    'Médecine interne': 'medecine',
    'Médecine légale': 'balance',
    'Médecine nucléaire': 'atome',
    'Médecine du travail': 'outil',
    'Médecine préventive': 'vaccin',
    'Gériatrie': 'vieux',
    'Douleur': 'douleur',
    'Nutrition': 'pomme',
    'Biologie médicale': 'microscope',
    'Anatomie et cytologie pathologiques': 'microscope',
}

def index(request):
    medecins   = Medecin.objects.all()
    specialites= Specialite.objects.all()

    # on ajoute l’image à chaque spécialité
    for spec in specialites:
        spec.image = SPEC_IMAGES.get(spec.nom, 'medecin')  # fallback

    # ----- filtres déjà présents -----
    spec_id = request.GET.get('specialite')
    if spec_id:
        medecins = medecins.filter(specialite_id=spec_id)

    ville_choisie = request.GET.get('ville')
    if ville_choisie:
        medecins = medecins.filter(ville=ville_choisie)
    # ---------------------------------

    return render(request, 'pages/index.html', {
        'medecins': medecins,
        'specialites': specialites,
        'villes': WILAYAS_CHOICES,
        'current_ville': ville_choisie,
        'current_spec': int(spec_id) if spec_id else None,
    })


