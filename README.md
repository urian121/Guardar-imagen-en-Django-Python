# 🔥 Guardar archivo imagen en Django Python 🐍

###### 1. Crear un entorno virtual, hay muchas formas

    Opción 1: Crear entorno virtual con el paquete virtualenv,
    puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/

    pip install virtualenv #Instalar paquete virtualenv
    virtualenv --version #Version
    virtualenv env #Crear entorno con el paquete virtualenv

    Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
    python -m venv env

###### 2. Activar ambiente virtual

      . env/Script/activate
     Para desactivar mi entorno virtual  ` deactivate`

###### 3. Instalar Djando desde el manejador de paquete de Python Pip

    pip install Django
    Nota: para instalar Django en una version especifica
    pip install Django==4.2.4

###### 4. Instalar el paquete (biblioteca) Pillow, esto con el fin de poder procesar la subida de imagen en el servidor

    Pillow es la librería que nos permitirá usar el campo ImageField para poder guardar imágenes

    - https://pypi.org/project/Pillow/
      pip install Pillow

###### 6. Crear el proyecto con Djando

    `django-admin startproject project_core .`
    El punto . es crucial le dice al script que instale Django en el directorio actual

     Ya en este punto se puede correr el proyecto que a creado Django,
      python manage.py runserver

###### 7. Crear mi primera aplicación en Django

    python manage.py startapp upload_img

###### 8. Crear el archivo requirements.txt para tener todos mis paquetes a la mano

    pip freeze > requirements.txt
    Nota: para instalar los paquetes solo basta ejecutar
    pip install -r requirements.txt

###### 9. Instalar nuestra aplicación (upload_img) ya creada en el proyecto

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

#### 4. Creando y corriendo las migraciones

    python3 manager.py makemigrations <nombre del modelo> #Creando las migraciones de mi modelo
    python3 manager.py migrate #Correr migraciones

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

#### 6. Define el views.py

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

#### 7. Pintando el formulario en tu plantilla index.html

    <form method="post" enctype="multipart/form-data">
        {% csrf_token %} {{ form.as_p }}
        <button class="btn btn-primary" type="submit">subir imagen</button>
    </form>

##### Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/guardar-imagen-en-django-python-urian-viera.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
