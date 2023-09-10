from django import forms
from .models import Zapato


class ZapatoForm(forms.ModelForm):

    class Meta:
        model = Zapato
        # fields = '__all__'
        # fields = ('name', 'img_zapato')
        fields = ['name', 'img_zapato']
        labels = {
            'name': 'Nombre de la Imagen',
            'img_zapato': 'Imagen'
        }
