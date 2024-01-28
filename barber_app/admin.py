from django.contrib import admin
from .models import Cita, Cliente, Encuesta, Peluquero

# Agregar los modelos al administrador Django
admin.site.register(Cliente)
admin.site.register(Peluquero)
admin.site.register(Encuesta)
admin.site.register(Cita)