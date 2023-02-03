# FlaskApi

## Proyecto api rest con Flask creado por Bastián carreño

### Para iniciar el proyecto utiliza el siguiente comando:
```
python index.py
```

### A continuacón se listaran las funciones principales de la api y sus respectivos `endpoints`:

## servicio para crear instituciones
```
http://127.0.0.1:5000/crear/institucion
```
Esta función necesita del metodo `POST` y de un `Json` para poder crear un objeto Institucion en la base de datos.
ejemplo de json:
```
{
    "nombre": "Institución 1",
    "descripcion": "Descripcion de la Institución 1",
    "direccion": "Santiago Maipú",
    "fecha_creacion":"2020-09-12" 
}
```

## servicio para actualizar instituciones
```
http://127.0.0.1:5000/institucion/<int:institucion_id>/actualizar
```
Esta función necesita del metodo `PUT` para actualizar una institucion, en donde `institucion_id` corresponde a la **id** de la institución.
ejemplo de json:
```
{
    "nombre": "Institución 2",
    "descripcion": "Descripcion de la Institución 2",
    "direccion": "Santiago Maipú",
    "fecha_creacion":"2020-09-12" 
}
```


## servicio para listar instituciones
```
http://127.0.0.1:5000/ver/instituciones
```
Esta función necesita del metodo `GET` para listar todas las Instituciones de la base de datos en un formato Json



## servicio para eliminar instituciones
```
http://127.0.0.1:5000/institucion/<int:institucion_id>/actualizar
```
Esta función necesita del metodo `DELETE` para liminar una institucion, en donde `institucion_id` corresponde a la **id** de la institución.


## servicio para listar todos los proyectos de una instituciones
```
http://127.0.0.1:5000/institucion/<int:institucion_id>/proyectos
```
Esta función necesita del metodo `GET` para listar todos los proyectos de una institucion, en donde `institucion_id` corresponde a la **id** de la institución dando como resultado una respuesta en formato JSON con los datos de la institución y sus respectivos proyectos


## servicio para listar las direcciones de las instituciones agregando a la dirección una url para acceder a google maps
```
http://127.0.0.1:5000/ver/instituciones/maps
```
Esta función necesita del metodo `GET` para listar todas las direcciones de las Instituciones de la base de datos en un formato Json

## servicio para listar un usuario (filtro por Rut) con sus respectivos proyectos.
```
http://127.0.0.1:5000/ver/usuario/<string:rut>/proyectos
```

Esta función necesita del metodo `GET` para listar un Usuario, en donde `rut` corresponde a la **RUT** del usuario.

## servicio para listar los proyectos que la respuesta sea el nombre del proyecto y los días que faltan para su término.

```
http://127.0.0.1:5000/ver/proyectos/termino
```

Esta función necesita del metodo `GET` para listar los proyectos en un formato json
