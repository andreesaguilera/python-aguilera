# AGUILERA Andres - Curso CODERHOUSE Python

Pre-entrega del curso de Python en CoderHouse

## Instalación

1. Forkeá y cloná el repositorio

2. Parado en la raíz del proyecto ejecutar 

   ```
   pip install virtualenv
   ```
    para instalar virtualenv

3. Luego Ejecutar 

   ```
   virtualenv venv
   ```

    para crear un entorno virtual

4. Activar el interprete  

5. Ejecutar

    ```
    pip install django
    ```
    
    para instalar django

6. Ejecutar

    ```
    pip install pillow
    ```
    
    para instalar pillow


7. moverse a la carpeta del proyecto ejecutando

    ```
    cd aguilera
    ```

8. Ejecutar

    ```
    python manage.py runserver
    ```

    para levantar el servidor

9. Abrir el navegador en la dirección http://localhost:8000/
    
 


## Uso

El proyecto cuenta con tres modelos. Viviendas en venta, Viviendas en alquiler y Clientes

Rutas: 
 - /ventas/list-ventas/ para visualizar las viviendas en venta
 - /ventas/create-venta/ para crear una vivienda en venta (Solo Admin)
 - /ventas/edit-venta/:id para editar una vivienda en venta (Solo Admin) 
 - /ventas/delet-venta/:id para eliminar una vivienda en venta (Solo Admin) 
 - /alquileres/list-alquileres/ para visualizar las viviendas en alquiler
 - /alquileres/create-alquiler/ para crear una vivienda en alquiler (Solo Admin)
 - /alquileres/edit-alquiler/:id para editar una vivienda en alquiler (Solo Admin)
 - /alquileres/delet-alquiler/:id para eliminar una vivienda en alquiler (Solo Admin)
 - /clientes/list-clientes/ para visualizar los clientes (Solo Admin)
 - /clientes/edit-cliente/:id para editar un clientes (Solo Admin)
 - /clientes/delet-cliente/:id para eliminar un clientes (Solo Admin)
 - /users/profile para ver la vista del usuario
 - /users/edit para editar los datos de usuario
 - /users/update para editar los datos de perfil

 Para poder ver el listado de viviendas en Alquiler o venta, es necesario estar logueado.
 Para poder editar o eliminar las viviendas, es necesario estar logueado como administrador.
 Para poder ver, editar y/o borrar clientes, es necesario estar logueado como administrador.

 Al ingresar como administrador se abilitan los botones para acceder a editar o eliminar datos.
 

En el buscador del Navbar se pueden buscar las viviendas en alquiler

Para acceder al panel de administrador usar el Usuario Andres y el Pass andrespass

