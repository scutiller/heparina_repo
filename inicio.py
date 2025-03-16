class BombaHeparina:
    def __init__(self, nombre_paciente, peso):
        self.nombre_paciente = nombre_paciente.replace(",", " ")  # Corrige nombre si tiene coma
        self.peso = peso
        self.volumen = None  # Inicializar volumen en None
    
    def set_bomba(self, volumen):
        self.volumen = volumen

    def get_preparacion(self):
        if self.volumen is None:
            return "Error: El volumen no ha sido establecido. Use set_bomba()."
        
        unidades_heparina = self.peso * self.volumen
        concentracion = unidades_heparina / self.volumen
        bolo = self.peso * 80

        return (
            f'Colocar {unidades_heparina} UI de heparina en {self.volumen} ml de solución fisiológica '
            f'para obtener una solución de {concentracion} UI/ml de Heparina Sódica. '
            f'El bolo inicial debería ser de {bolo} UI.'
        )

    def ajusta_bomba(self, infusion_actual, kptt):
        """ Ajusta la infusión según el valor de kPTT """
        if kptt < 40:
            return f'Administrar bolo de {25 * self.peso} UI y configurar la bomba a {infusion_actual + 3} ml/hr'
        elif 40 <= kptt <= 50:
            return f'Configurar la bomba a {infusion_actual + 2} ml/hr'
        elif 50 < kptt <= 69:
            return f'Configurar la bomba a {infusion_actual + 1} ml/hr'
        elif 70 <= kptt <= 110:
            return 'RANGO TERAPÉUTICO ALCANZADO.'
        elif 111 <= kptt <= 120:
            return f'Configurar la bomba a {infusion_actual - 1} ml/hr'
        elif 120 < kptt <= 130:
            return f'DETENER INFUSIÓN POR UNA HORA. Configurar la bomba a {infusion_actual - 2} ml/hr'
        elif 131 <= kptt <= 140:
            return f'DETENER INFUSIÓN POR UNA HORA. Configurar la bomba a {infusion_actual - 3} ml/hr'
        elif 141 <= kptt <= 150:
            return f'DETENER INFUSIÓN POR DOS HORAS. Configurar la bomba a {infusion_actual - 4} ml/hr'
        elif kptt > 150:
            return f'DETENER INFUSIÓN POR DOS HORAS. Configurar la bomba a {infusion_actual - 5} ml/hr'










