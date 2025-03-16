from django.shortcuts import render

from django.shortcuts import render
from .forms import BombaHeparinaForm
from .models import BombaHeparina

def calcular_bomba(request):
    resultado_preparacion = None
    resultado_ajuste = None

    if request.method == "POST":
        form = BombaHeparinaForm(request.POST)
        if form.is_valid():
            bomba = form.save(commit=False)
            resultado_preparacion = bomba.get_preparacion()
            resultado_ajuste = bomba.ajusta_bomba()
    else:
        form = BombaHeparinaForm()

    return render(request, "calculos/calcular_bomba.html", {
        "form": form,
        "resultado_preparacion": resultado_preparacion,
        "resultado_ajuste": resultado_ajuste
    })

