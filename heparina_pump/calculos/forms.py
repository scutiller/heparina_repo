from django import forms
from .models import BombaHeparina

class BombaHeparinaForm(forms.ModelForm):
    class Meta:
        model = BombaHeparina
        fields = ['nombre_paciente', 'peso', 'volumen', 'infusion_actual', 'kptt']
