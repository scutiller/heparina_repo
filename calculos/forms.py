from django import forms
from .models import BombaHeparina

class BombaHeparinaForm(forms.ModelForm):
    class Meta:
        model = BombaHeparina
        fields = ['nombre_paciente', 'peso', 'volumen', 'infusion_actual', 'kptt']
                
        labels = {
            'nombre_paciente': 'Nombre del Paciente',
            'peso': 'Peso del Paciente (kg)',
            'volumen': 'Volumen de Solución (ml)',
            'infusion_actual': 'Infusión Actual (ml/hr)',
            'kptt': 'Tiempo de Tromboplastina Parcial Activado (kPTT)',
        }
