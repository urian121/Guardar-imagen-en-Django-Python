from django.urls import path
# from . views import hotel_image_view, success, list_imagenes, inicio
from . import views


urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('', views.hotel_image_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('lista', views.list_imagenes, name='lista'),
]
