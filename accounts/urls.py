from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Vue personnalisée pour l'inscription
    path('inscription/', views.inscription, name='inscription'),
    
    # Vue personnalisée pour le tableau de bord
    path('mon-espace/', views.dashboard, name='dashboard'),

    # Vues intégrées de Django pour Login/Logout
    path('connexion/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='logout'),
]