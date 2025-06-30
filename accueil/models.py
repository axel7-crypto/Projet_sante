from django.db import models

# Create your models here.
from django.db import models

class Signalement(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    type_probleme = models.CharField(max_length=100)
    description = models.TextField()
    localisation = models.CharField(max_length=255)
    date_signalement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.type_probleme}"
