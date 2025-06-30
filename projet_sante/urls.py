from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accueil.urls')),  # 👈 Lien vers la page d'accueil
]
