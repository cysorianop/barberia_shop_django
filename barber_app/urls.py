from django.urls import path
from . import views

# insertar las urls de cada accion de la api
# Tener en cuenta nombrarlas de una manera clara para no confundirse
urlpatterns = [
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar-peluquero/', views.agregar_peluquero, name='agregar_peluquero'),
    path('reservar-cita/', views.reservar_cita, name='reservar_cita'),
    path('completar-cita/<int:cita_id>/', views.completar_cita, name='completar_cita'),
    path('crear-encuesta/<int:cita_id>/', views.crear_encuesta, name='crear_encuesta')
]