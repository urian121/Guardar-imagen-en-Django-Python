from django.urls import path
# from . views import hotel_image_view, success, list_imagenes, inicio
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
]
