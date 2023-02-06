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

6. moverse a la carpeta del proyecto ejecutando

    ```
    cd aguilera
    ```

7. Ejecutar

    ```
    python manage.py runserver
    ```

    para levantar el servidor

8. Abrir el navegador en la dirección http://localhost:8000/
    
 


## Uso

El proyecto cuenta con tres modelos. Viviendas en venta, Viviendas en alquiler y Alquileres temporales

Rutas: 
 - /ventas/list-ventas/ para visualizar las viviendas en venta
 - /ventas/create-venta/ para crear una vivienda en venta
 - /alquileres/list-alquileres/ para visualizar las viviendas en alquiler
 - /alquileres/create-alquiler/ para crear una vivienda en alquiler
 - /temporales/list-temporales/ para visualizar las viviendas en alquiler temporales
 - /temporales/create-temporal/ para crear una vivienda en alquiler temporal

En el buscador del Navbar se pueden buscar las viviendas en alquiler

Para acceder al panel de administrador usar el Usuario Andres y el Pass andrespass

