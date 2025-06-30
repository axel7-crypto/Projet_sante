from django import forms
from .models import Signalement

class SignalementForm(forms.ModelForm):
    class Meta:
        model = Signalement
        fields = ['nom', 'telephone', 'type_probleme', 'description', 'localisation']
