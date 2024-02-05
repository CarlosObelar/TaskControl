# TaskControl
TaskControl es una página web diseñada para ayudarte a organizar tus tareas y actividades de manera eficiente. Con funcionalidades principales de un CRUD (Crear, Leer, Actualizar, Borrar), TaskControl te permite gestionar tus tareas de forma sencilla y rápida.

## Características principales
- Registro e inicio de sesión de usuarios: Crea una cuenta para comenzar a utilizar TaskControl y accede fácilmente a tus tareas desde cualquier lugar.

- Gestión de tareas: Agrega, lee, actualiza y elimina tareas según tus necesidades. Cada tarea incluye la fecha de creación, una descripción, estado de la tarea y un comentario opcional.

- Estado de la tarea: Las tareas pueden tener uno de los siguientes estados:

  - Done: Si la tarea ha sido completada, puedes marcarla como "Done" presionando un botón.
  - Pending: Si la fecha de la tarea es posterior a la fecha actual, se mostrará como "Pending".
  - Undone: Si la fecha de la tarea ya ha pasado y no ha sido marcada como "Done", se mostrará como "Undone".

## Tecnologías utilizadas
- Frontend: HTML, CSS
- Backend: Python (utilizando Flask)
- Base de datos: SQLite
- Librerías: datetime (para la gestión de fechas)

## Instrucciones de uso
- Registro e inicio de sesión:
Crea una cuenta en TaskControl o inicia sesión si ya tienes una cuenta existente.

- Gestión de tareas:
  - Agregar tarea: Haz clic en el botón azul con un simbolo (+) en el apartado con el título 'Add a new task' y completa el formulario con la descripción y fecha de la tarea (el comentario es opcional).
  - Actualizar tarea: Haz clic en el botón azul con un lápiz junto a la tarea que deseas actualizar y modifica los detalles según sea necesario.
  - Eliminar tarea: Para eliminar una tarea, haz clic en el botón rojo con un basurero junto a la tarea correspondiente.

- Estado de la tarea:
Marca una tarea como "Done" si ha sido completada presionando el botón verde con un check que esta al lado de dicha tarea.
Las tareas se clasificarán automáticamente como "Pending" si la fecha ingresada es posterior a la fecha actual y como "Undone" si la fecha ya ha pasado y no se ha marcado como "Done".

- Cerrar sesión:
Para proteger tu información, asegúrate de cerrar sesión una vez hayas terminado de utilizar TaskControl.

## Contribución
Si deseas contribuir a TaskControl, ¡estamos abiertos a colaboraciones! Siéntete libre de bifurcar este repositorio, realizar cambios y enviar solicitudes de extracción.
