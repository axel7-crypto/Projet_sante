from django.urls import path
from .views import accueil_view

urlpatterns = [
    path('', accueil_view, name='accueil'),
]

from django.urls import path
from .views import accueil_view, formulaire_signalement

urlpatterns = [
    path('', accueil_view, name='accueil'),
    path('signaler/', formulaire_signalement, name='formulaire_signalement'),
]
