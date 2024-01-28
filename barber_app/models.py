from django.db import models

# Create your models here.
class Cliente(models.Model):
    """
    Modelo para almacenar información de los clientes.

    Fields:
    - nombre (CharField): Nombre del cliente.
    - telefono (CharField): Número de teléfono del cliente.
    - email (EmailField): Dirección de correo electrónico única del cliente.

    Methods:
    - __str__: Devuelve una representación de cadena del cliente (nombre).
    """
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
class Peluquero(models.Model):
    """
    Modelo para almacenar información de los peluqueros.

    Fields:
    - nombre (CharField): Nombre del peluquero.
    - servicios (TextField): Descripción de los servicios ofrecidos por el peluquero.

    Methods:
    - __str__: Devuelve una representación de cadena del peluquero (nombre).
    """
    nombre = models.CharField(max_length=100)
    servicios = models.TextField()

    def __str__(self):
        return self.nombre
    
class Cita(models.Model):
    """
    Modelo para almacenar información de las citas.

    Fields:
    - cliente (ForeignKey): Cliente asociado a la cita.
    - peluquero (ForeignKey): Peluquero asociado a la cita.
    - servicio_elegido (CharField): Descripción del servicio elegido para la cita.
    - fecha_hora (DateTimeField): Fecha y hora de la cita.
    - completada (BooleanField): Indica si la cita ha sido completada.

    Methods:
    - __str__: Devuelve una representación de cadena de la cita.

    """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    peluquero = models.ForeignKey(Peluquero, on_delete=models.CASCADE)
    servicio_elegido = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"Cita para {self.cliente} con {self.peluquero} el {self.fecha_hora}"

class Encuesta(models.Model):
    """
    Modelo para almacenar información de las encuestas asociadas a las citas.

    Fields:
    - cita (OneToOneField): Cita asociada a la encuesta.
    - calificacion (IntegerField): Calificación numérica de la cita.
    - comentario (TextField): Comentario opcional sobre la cita.

    Methods:
    - __str__: Devuelve una representación de cadena de la encuesta.
    """
    cita = models.OneToOneField('Cita', on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Encuesta para {self.cita} - Calificación: {self.calificacion}"
