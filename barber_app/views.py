from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from barber_app.models import Cita, Encuesta
from .forms import ClienteForm, PeluqueroForm, CitaForm, EncuestaForm, CompletarCitaForm

def agregar_cliente(request):
    """
    Vista para agregar un nuevo cliente.

    - Método GET: Muestra el formulario para agregar un cliente.
    - Método POST: Procesa el formulario y guarda el cliente en la base de datos.

    Returns:
    - HttpResponse: Mensaje indicando si el cliente fue creado correctamente o si el método no es soportado.
    """
    if request.method == 'POST':
        print("Solicitud POST recibida para agregar_cliente")
        clienteForm = ClienteForm(request.POST)
        if clienteForm.is_valid():
            clienteForm.save()
            return HttpResponse("Cliente creado correctamente")
    else:
        print("Solicitud GET recibida para agregar_cliente")
        clienteForm = ClienteForm()
        return render(request, 'agregarCliente.html', {'clienteForm': clienteForm})    
    return HttpResponse('Metodo no soportado')
    
def agregar_peluquero(request):
    """
    Vista para agregar un nuevo peluquero.

    - Método GET: Muestra el formulario para agregar un peluquero.
    - Método POST: Procesa el formulario y guarda el peluquero en la base de datos.

    Returns:
    - HttpResponse: Mensaje indicando si el peluquero fue creado correctamente o si el método no es soportado.
    """
    if request.method == 'POST':
        print("Solicitud POST recibida para agregar_peluquero")
        peluqueroForm = PeluqueroForm(request.POST)
        if peluqueroForm.is_valid():
            peluqueroForm.save()
            return HttpResponse("Peluquero creado correctamente")
    else:
        print("Solicitud GET recibida para agregar_peluquero")
        peluqueroForm = PeluqueroForm()
        return render(request, 'agregarPeluquero.html', {'peluqueroForm': peluqueroForm})
    return HttpResponse('Metodo no soportado')

def reservar_cita(request):
    """
    Vista para reservar una cita.

    - Método GET: Muestra el formulario para reservar una cita.
    - Método POST: Procesa el formulario, guarda la cita en la base de datos y envía un correo de confirmación.
    - utiliza send_mail de Django para el envio de correos electronicos, como es un entorno de prueba se simula el envio de dicho correo
    Returns:
    - HttpResponse: Mensaje indicando si la cita fue reservada correctamente, si el método no es soportado o el formulario en caso de error.
    """
    if request.method == 'POST':
        cita_form = CitaForm(request.POST)
        if cita_form.is_valid():
            cita = cita_form.save()
            # Enviar correo de confirmacion
            send_mail(
                'Confirmación de Cita',
                'Tu cita ha sido reservada con éxito.',
                'cysp97@example.com',  # Cambia esto con tu dirección de correo electrónico
                [cita.cliente.email],  # Usa el correo electrónico del cliente de la cita
                fail_silently=False,
            )

            return HttpResponse("Cita reservada correctamente y correo de confirmación enviado.")
    else:
        cita_form = CitaForm()
        return render(request, 'reservarCita.html', {'cita_form': cita_form})
    return HttpResponse('Metodo no soportado')

    
def completar_cita(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)

    if request.method == 'POST':
        completar_cita_form = CompletarCitaForm(request.POST, instance=cita)
        if completar_cita_form.is_valid():
            completar_cita_form.save()
            return HttpResponse("Cita completada correctamente")
    else:
        completar_cita_form = CompletarCitaForm(instance=cita)
        return render(request, 'completarCita.html', {'completar_cita_form': completar_cita_form, 'cita': cita})
    HttpResponse('Metodo no soportado')


def crear_encuesta(request, cita_id):
    """
    Vista para completar una cita.

    - Método GET: Muestra el formulario para completar una cita.
    - Método POST: Procesa el formulario y actualiza el estado de la cita en la base de datos.

    Returns:
    - HttpResponse: Mensaje indicando si la cita fue completada correctamente, o el formulario en caso de error.
    """
    id_cita = get_object_or_404(Cita, pk=cita_id)

    if request.method == 'POST':
        encuesta_form = EncuestaForm(request.POST, instance=id_cita)
        if encuesta_form.is_valid():
            encuesta_form.save()
            return HttpResponse("Encuesta creada correctamente")
    else:
        encuesta_form = EncuestaForm(instance=id_cita)
        return render(request, 'crearEncuesta.html', {'encuesta_form': encuesta_form, 'cita': id_cita})
    return HttpResponse('Metodo no soportado')

def crear_encuesta(request, cita_id):
    """
    Vista para crear una encuesta asociada a una cita.

    - Método GET: Muestra el formulario para crear una encuesta.
    - Método POST: Procesa el formulario y guarda la encuesta en la base de datos.

    Returns:
    - HttpResponse: Mensaje indicando si la encuesta fue creada correctamente, o el formulario en caso de error.
    """
    cita = get_object_or_404(Cita, pk=cita_id)

    if request.method == 'POST':
        encuesta_form = EncuestaForm(request.POST)
        if encuesta_form.is_valid():
            encuesta = encuesta_form.save(commit=False)
            encuesta.cita = cita
            encuesta.save()
            return HttpResponse("Encuesta creada correctamente")
    else:
        encuesta_form = EncuestaForm()
        return render(request, 'crearEncuesta.html', {'encuesta_form': encuesta_form, 'cita': cita})
    return HttpResponse('Metodo no soportado')    
    

