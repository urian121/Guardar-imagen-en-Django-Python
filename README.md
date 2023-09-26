# 🔥 Guardar archivo imagen en Django Python 🐍

###### 1. Crear un entorno virtual, hay muchas formas

    Opción 1: Crear entorno virtual con el paquete virtualenv,
    puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/

    pip install virtualenv #Instalar paquete virtualenv
    virtualenv --version #Version
    virtualenv env #Crear entorno con el paquete virtualenv

    Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
    python -m venv env o python3 -m venv env

###### 2. Activar ambiente virtual

    . env/Script/activate #Activar ambiente desde Windows
    . env/bin/activate  #Activar desde la Mac
    deactivate #Desactivar mi entorno virtual

###### 3. Instalar Djando desde el manejador de paquete de Python Pip

    pip install Django
    Nota: para instalar Django en una version especifica
    pip install Django==4.2.4
    python3 -m django --version  #Vrsion instalada de Django

###### 4. Instalar el paquete (biblioteca) Pillow, esto con el fin de poder procesar la subida de imagen en el servidor

    Pillow es la librería que nos permitirá usar el campo ImageField para poder guardar imágenes

    https://pypi.org/project/Pillow/
    pip install Pillow

###### 5. Crear el proyecto con Djando

    `django-admin startproject project_core .`
     El punto . es crucial le dice al script que instale Django en el directorio actual

     Ya en este punto se puede correr el proyecto que a creado Django,
     python manage.py runserver

###### 6. Crear mi primera aplicación en Django

    python manage.py startapp upload_img

###### 7. Crear el archivo requirements.txt para tener todos mis paquetes a la mano

    pip freeze > requirements.txt
    pip install -r requirements.txt  #Para instalar los paquetes del proyecto

###### 8. Instalar nuestra aplicación (upload_img) ya creada en el proyecto

    archivo settings.py
    INSTALLED_APPS = [
    ----,
    'upload_img',
    ]

#### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

##### 1. Configurar el settings.py

    El módulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo.
    import os
    # Es la URL que podemos usar en nuestras plantillas para referenciar las imagenes.
    MEDIA_URL = '/media/'
    # Es la ruta absoluta del sistema donde se almacenará el archivo.
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    IMPORTANTE: crear una carpeta al mismo nivel del proyecto 'project_core' que se llame 'media' sera alli donde
    guardaremos las imagenes subidas.

#### 2. Configurar el archivo urls.py del proyecto

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
    	# tus urls
    ]

    if settings.DEBUG:
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#### 3. Definiendo el models.py

    from django.db import models

    class Zapato(models.Model):
        name = models.CharField(max_length=50)
        img_zapato = models.ImageField(upload_to='images/', null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)

        class Meta:
            db_table = "zapatos"
            ordering = ['-created_at']

#### 4. Creando y corriendo las migraciones

    python3 manage.py makemigrations <nombre del modelo> #Creando las migraciones de mi modelo
    python3 manage.py migrate #Correr migraciones

#### 5. Definiendo el forms.py

    from django import forms
    from .models import *

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

#### 6. Crear archivo urls.py para manejar las rutas de mi aplicacion

    from django.urls import pathess, list_imagenes, inicio
    from . import views

    urlpatterns = [
        path('', views.inicio, name='inicio'),
    ]

#### 7. Importar el archivo urls.py de nuestra aplicacion en urls.py del proyecto

    from django.urls import path, include  # nuevo

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('upload_img.urls')),
    ]

#### 8. Define el views.py

    # Importando el modelo
    from .models import Zapato

    # Importando el formulario desde la instacia de modelo forms
    from .forms import ZapatoForm

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

#### 9. Pintando el formulario en tu plantilla index.html

    <form method="post" enctype="multipart/form-data">
        {% csrf_token %} {{ form.as_p }}
        <button class="btn btn-primary" type="submit">subir imagen</button>
    </form>

#### 10. Corriendo el proyecto

    python3 manage.py runserver # Corriendo el proyecto
    python3 manage.py runserver 8500 #Corriendo el proyecto en un puerto diferente

## Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/guardar-imagen-en-django-python-urian-viera.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
