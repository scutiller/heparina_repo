from django import forms
from .models import BombaHeparina

class BombaHeparinaForm(forms.ModelForm):
    class Meta:
        model = BombaHeparina
        fields = ['peso', 'volumen', 'infusion_actual', 'kptt']
                
        labels = {
            'peso': 'Peso del Paciente (kg)',
            'volumen': 'Volumen de Solución (ml)',
            'infusion_actual': 'Infusión Actual (ml/hr)',
            'kptt': 'Tiempo de Tromboplastina Parcial Activado (kPTT)',
        }
