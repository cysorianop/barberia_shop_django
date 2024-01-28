## Api barberia shop - Reserva de citas

En que consiste este proyecto:
- Administrar clientes, peluqueros y citas
- Crear clientes, peluqueros y permitir la creacion de citas
- Validar la hora elegida por el cliente y la disponibilidad del peluquero
- Permitir al peluquero dar por completada la cita de un cliente
- Crear una encuesta de satisfacion de cliente hacia el servicio contratado

## Requerimientos

Una vez descargado el repositorio, se debe tener instalado:
- Python 3.12.1
- Django 5.0.1

## Iniciar proyecto

Al iniciar el proyecto se debe tener en cuenta:

- El proyecto esta configurado para poder observar los cambios en la base de datos desde el administrador Django, para esto se debe configurar el super usuario:

```
python manage.py createsuperuser
```

- Crear las migraciones: 

```
python manage.py makemigrations
```

- Aplicar las migraciones:

```
python manage.py migrate
```

- Iniciar el servidor después de este paso debe:

```
python manage.py runserver 
```

## Funcionamiento

En cada url suministrada se permite realizar una accion, ya sea de creacion, check o reservar:
- Para la cada una de ellas se muestra un formulario el cual debe ser llenado por completo si es necesario, posteriormente al dar click en cada una de las acciones se remiten dos opciones:
    - Se guardan los registros en la base de datos.
    - Se muestra nuevamente el formulario(vacio).

Si el metodo utilizado falla, se enviara un mensaje de "Metodo no soportado" al cliente.

- Si el formulario es exitoso, se podra observar el cambio en la base de datos mediante el administrador de Django.


## Urls

Para ingresar al administrador de Django, vaya a la siguiente dirección:
[[http://localhost:8000/admin](http://localhost:8000/admin)]

Para ver si todo está funcionando como se espera, vaya a la siguiente dirección:
[[http://localhost:8000/agregar-cliente/](http://localhost:8000/agregar-cliente/)]
[[http://localhost:8000/agregar-peluquero/](http://localhost:8000/agregar-peluquero/)]
[[http://localhost:8000/reservar-cita/](http://localhost:8000/reservar-cita/)]
[[http://localhost:8000/completar-cita/<id_cita>/](http://localhost:8000/completar-cita/<id_cita>/)]
[[http://localhost:8000/crear-encuesta/<id_cita>/](http://localhost:8000/crear-encuesta/<id_cita>/)]

## Mejoras

¡Nos encantaría que te involucraras y contribuiras al proyecto! Aquí hay algunas maneras en que puedes contribuir:

- Reportar Problemas: Si encuentras problemas o errores, por favor crea un nuevo número aquí .

- Solicitudes de Extracción: Si deseas mejorar o agregar nuevas características, ¡estaríamos encantados de recibir solicitudes de extracción!

- Pruebas: Ayúdanos a mejorar la calidad del código proporcionando pruebas y asegurándote de que todo funciona correctamente.

- Comentarios: Queremos saber tu opinión. Si tienes sugerencias o ideas, por favor compártelas.





