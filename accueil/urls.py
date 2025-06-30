from django.urls import path
from .views import accueil_view

urlpatterns = [
    path('', accueil_view, name='accueil'),
]
