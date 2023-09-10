from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Importando el modelo
from .models import Zapato
# Importando el formulario desde la instacia de modelo forms
from .forms import ZapatoForm


# Create your views here.
def inicio(request):
    if request.method == 'POST':
        form = ZapatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('La imagen fue registrada con exito'))
            return redirect('inicio')
        else:
            messages.error(request, 'Error, no se pudo registrar la imagen.')
            return redirect("inicio")
    else:
        form = ZapatoForm()
        data = {
            'form': form,
            'zapatos': list_imagenes(request)
        }
    return render(request, 'index.html', data)


def list_imagenes(request):
    return Zapato.objects.all()


"""
def list_imagenes(request):
    zapatos = Zapato.objects.all()
    return render(request, 'list.html', {'zapatos': zapatos})
"""
