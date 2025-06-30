from django.http import HttpResponse

def accueil_view(request):
    return HttpResponse("<h1>Bienvenue sur l'application Santé CI 🚑</h1>")
