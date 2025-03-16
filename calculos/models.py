from django.db import models

class BombaHeparina(models.Model):
    
    peso = models.FloatField()
    volumen = models.FloatField(null=True, blank=True)
    infusion_actual = models.FloatField(null=True, blank=True)
    kptt = models.FloatField(null=True, blank=True)

    def get_preparacion(self):
        """Calcula la preparación de la bomba de heparina."""
        if self.volumen is None:
            return "Error: El volumen no ha sido establecido."
        
        unidades_heparina = self.peso * self.volumen
        concentracion = unidades_heparina / self.volumen
        bolo = min(self.peso * 80, 10000)  # Máximo bolo de 10,000 UI

        return (
            f'Colocar {unidades_heparina} UI de heparina en {self.volumen} ml de solución fisiológica '
            f'para obtener una solución de {concentracion} UI/ml de Heparina Sódica. '
            f'El bolo inicial debería ser de {bolo} UI.'
        )

    def ajusta_bomba(self):
        """Ajusta la infusión de la bomba según el valor de kPTT."""
        if self.kptt is None or self.infusion_actual is None:
            return "Error: Datos insuficientes para ajuste."
        
        ajuste = 0
        mensaje = ""

        if self.kptt < 40:
            ajuste = 3
            mensaje = f'Administrar bolo de {25 * self.peso} UI y configurar la bomba a '
        elif 40 <= self.kptt <= 50:
            ajuste = 2
            mensaje = "Configurar la bomba a "
        elif 50 < self.kptt <= 69:
            ajuste = 1
            mensaje = "Configurar la bomba a "
        elif 70 <= self.kptt <= 110:
            return 'RANGO TERAPÉUTICO ALCANZADO.'
        elif 111 <= self.kptt <= 120:
            ajuste = -1
            mensaje = "Configurar la bomba a "
        elif 120 < self.kptt <= 130:
            ajuste = -2
            mensaje = "DETENER INFUSIÓN POR UNA HORA. Configurar la bomba a "
        elif 131 <= self.kptt <= 140:
            ajuste = -3
            mensaje = "DETENER INFUSIÓN POR UNA HORA. Configurar la bomba a "
        elif 141 <= self.kptt <= 150:
            ajuste = -4
            mensaje = "DETENER INFUSIÓN POR DOS HORAS. Configurar la bomba a "
        elif self.kptt > 150:
            ajuste = -5
            mensaje = "DETENER INFUSIÓN POR DOS HORAS. Configurar la bomba a "

        nueva_inf = self.nueva_infusion(self.infusion_actual, ajuste)
        return f"{mensaje}{nueva_inf[0]} ml/hr ({nueva_inf[1]} UI/Kg/Hr - {nueva_inf[2]} UI/Hr)"

    def nueva_infusion(self, actual, incremento):
        """
        Calcula la nueva infusión asegurando que no se pase de 2000 UI/hr.
        Retorna una lista con [ml/hr, UI/Kg/hr, UI/hr].
        """
        nueva_inf_ml_hr = actual + incremento  # Nueva infusión en ml/hr
        
        # Asegurar que el volumen esté definido
        if self.volumen is None or self.volumen == 0:
            return "Error: No se ha establecido el volumen de infusión."

        concentracion = (self.peso * self.volumen) / self.volumen  # UI/ml
        nueva_ui_hr = nueva_inf_ml_hr * concentracion  # Total de UI/hr
        nueva_ui_kg_hr = nueva_ui_hr / self.peso  # UI/Kg/Hr

        if nueva_ui_hr > 2000:  # Si excede el límite de 2000 UI/hr, ajustar
            nueva_ui_hr = 2000
            nueva_inf_ml_hr = nueva_ui_hr / concentracion  # Ajusta el flujo en ml/hr
            nueva_ui_kg_hr = nueva_ui_hr / self.peso  # Ajusta la UI/Kg/hr

        return [round(nueva_inf_ml_hr, 2), round(nueva_ui_kg_hr, 2), round(nueva_ui_hr, 2)]

    def __str__(self):
        return f"{self.nombre_paciente} - {self.peso} kg"


