from django.http import HttpResponse

def accueil_view(request):
    return HttpResponse("<h1>Bienvenue sur l'application Santé CI 🚑</h1>")

from django.shortcuts import render, redirect
from .forms import SignalementForm

def formulaire_signalement(request):
    if request.method == 'POST':
        form = SignalementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Signalement enregistré avec succès ✅")
    else:
        form = SignalementForm()
    return render(request, 'accueil/formulaire.html', {'form': form})
