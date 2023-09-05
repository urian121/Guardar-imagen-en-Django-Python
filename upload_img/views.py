from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Importando el modelo
from .models import Zapato
# Importando el formulario desde la instacia de modelo forms
from .forms import ZapatoForm


def inicio(request):
    form = ZapatoForm()
    return render(request, 'demo.html', {'form': form})


# Create your views here.
def hotel_image_view(request):
    if request.method == 'POST':
        form = ZapatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your movie was successfully added!'))
            return redirect('success')
        else:
            messages.error(request, 'Error saving form')
            return redirect("inicio")
    else:
        form = ZapatoForm()
    return render(request, 'index.html', {'form': form})


def list_imagenes(request):
    zapatos = Zapato.objects.all()
    return render(request, 'list.html', {'zapatos': zapatos})


def success(request):
    return HttpResponse('successfully uploaded')
