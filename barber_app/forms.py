from django.forms import ModelForm
from .models import Cliente, Peluquero, Cita, Encuesta
from django.core.exceptions import ValidationError

class ClienteForm(ModelForm):
    """
    Formulario para el modelo Cliente.

    Fields:
    - nombre: Nombre del cliente.
    - telefono: Número de teléfono del cliente.
    - email: Dirección de correo electrónico única del cliente.
    """
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']

class PeluqueroForm(ModelForm):
    """
    Formulario para el modelo Peluquero.

    Fields:
    - nombre: Nombre del peluquero.
    - servicios: Descripción de los servicios ofrecidos por el peluquero.
    """
    class Meta:
        model = Peluquero
        fields = ['nombre', 'servicios']

class CitaForm(ModelForm):
    """
    Formulario para el modelo Cita.

    Fields:
    - cliente: Cliente asociado a la cita.
    - peluquero: Peluquero asociado a la cita.
    - servicio_elegido: Descripción del servicio elegido.
    - fecha_hora: Fecha y hora de la cita.
    - completada: Indica si la cita ha sido completada.

    Custom validation:
    - Verifica la disponibilidad del peluquero en la fecha y hora seleccionadas.
    """
    class Meta:
        model = Cita
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_hora = cleaned_data.get('fecha_hora')
        peluquero = cleaned_data.get('peluquero')

        # Verificar disponibilidad del peluquero dentro del formulario HTML
        if Cita.objects.filter(peluquero=peluquero, fecha_hora=fecha_hora).exists():
            raise ValidationError("El peluquero no está disponible en ese horario")

        return cleaned_data

class EncuestaForm(ModelForm):
    """
    Formulario para el modelo Encuesta.

    Fields:
    - cita: Cita asociada a la encuesta.
    - calificacion: Calificación numérica de la cita.
    - comentario: Comentario opcional sobre la cita.

    Custom validation:
    - Verifica si ya existe una encuesta asociada a la cita.
    """
    class Meta:
        model = Encuesta
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        cita = cleaned_data.get('cita')

        # Verificar si la cita ya tiene una encuesta asociada dentro del formulario HTML
        if Encuesta.objects.filter(cita=cita).exists():
            raise ValidationError("Ya se ha creado una encuesta para esta cita.")
        
        return cleaned_data

class CompletarCitaForm(ModelForm):
    """
    Formulario para completar una cita.

    Fields:
    - completada: Indica si la cita ha sido completada.

    Se utiliza para completar una cita existente en el sistema.
    """
    class Meta:
        model = Cita
        fields = ['completada']