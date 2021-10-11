# fire-app-cba

App para el informe y seguimiento de incendios y otros eventos atentidos por
los Bombla Provincia de Cordoba.

### Setup Inicial

1. Las dependencias para el proyecto se encuentran en el archivo environment.yml
    localizado en la carpeta raiz del proyecto.
2. Una vez creada la base de datos y realizado el deploy crear los modelos y migraciones correspondientes:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
3. Crear un SuperAdmin:
    ```
    python manage.py createsuperuser
    ```
4. Llamar al endpoint '/load_cuarteles/' para asi cargar todos los cuarteles en la base de datos.


### Usuarios

1. Los usuarios se crean desde el endpoint 'admin/users'.
2. Cada vez que se crea un User, tambien se crea automaticamente una instancia
    UserProfile. Para el correcto funcionamiento de la app es necesario que
    se asigne a cada usuario (incluido el superuser), en su UserProfile, el
    cuartel al cual pertenece ese usuario. Esto incluye al SuperUser.
    Esta asignacion se hace desde el endpoint 'admin/users/usersprofile'

-  Ademas del SuperAdmin, que tiene acceso irrestricto, se debe considerar un
  usuario con acceso a las pantallas de administrador que pueda cargar
  incendios y usuarios.
  Este usuario se obtiene marcando la celda "Staff status" en '/admin/auth/user/'.
  Por ultimo estan los usuarios que usan la aplicacion movil, que no tienen
  acceso a la pantalla de administrador. Para obtener estos usuarios basta con
  dejar desmarcada la celda "Staff status"
