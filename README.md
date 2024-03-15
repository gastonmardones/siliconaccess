# Silicon Access API
> API para el ignreso y egreso de vehículos


3 opciones: Local - Docker - Desplegado en producción


0. Clonar el repositorio
  ```shell Shell
  git clone https://github.com/gastonmardones/siliconaccess.git
  ```


## Local


1. Crear un entorno virtual (opcional)
  ```shell Shell
  # Instalar virtualenv si aún no está instalado
  pip install virtualenv
  
  # Crear un entorno virtual
  virtualenv env
  
  # Activar el entorno virtual
  # En Windows
  env\Scripts\activate
  # En macOS/Linux
  source env/bin/activate
  ```


2. Instalar dependencias
  ```shell Shell
  cd silicon_access
  pip install -r requirements.txt
  ```


3. Modificar el archivo .env agregando tus credenciales de postgres locales


4. Ejecutar migraciones
```shell Shell
python manage.py migrate
```


5. Ejecutar el servidor de desarrollo
``` shell Shell
python manage.py runserver
```



## Docker

1. Agregar las variables de entorno de postgres en el archivo docker-compose.


2. Construir y levantar el docker
``` shell Shell
docker-compose up -d
```


3. Acceder a http://127.0.0.1:8000/api/v1/

## Desplegado

https://siliconaccess.onrender.com/api/v1

> **Nota:** La URL o endpoint puede tener un retraso inicial considerable debido a que el servidor, al ser gratuito, se encuentra inactivo hasta su primer uso.




# Utilizar la API

## Requisitos
- Instalar un cliente HTTP como Postman.

### Autenticación
La API utiliza tokens de autenticación. Para obtener un token de acceso:
1. Envia una solicitud POST a siliconaccess.onrender.com/login/ con los parametros en body: username: silicon password: access (ya creados por default).
2. Recibirás un Token de acceso en la respuesta (copialo).

### Acceso a endpoints
Incluí el Token de acceso en el encabezado "Authorization" en todas las solicitudes siguientes.
Ejemplo en postman: En la pestaña "Headers" Key: Authorization | Value: Token {token}

### Endpoints disponibles
https://siliconaccess.onrender.com/api_documentation/
Ahí se encuentran todos los endpoints.

> **GET /api/v1/endpoint_type/:** Obtiene una lista de <endpoint_type>.

> **POST /api/v1/endpoint_type/:** Crea un <endpoint_type>.

> **GET /api/v1/endpoint_type/{pk}/:** Ve una instancia de <endpoint_type>.

> **PUT /api/v1/endpoint_type/{pk}/:** Edita una instancia de <endpoint_type>.

> **DELETE /api/v1/endpoint_type/{pk}/:** Elimina una instancia de <endpoint_type>.

> **endpoint_types:** [users, vehicle, vehicle_record, vehicle_type].


### Cierre de sesión

Para cerrar sesión y eliminar el token de acceso:
1. Envía una solicitud POST a https://siliconaccess.onrender.com/logout/ con el parametro token en la URL, con el valor de tu token de acceso.
   
    Ejemplo en postman: En la pestaña params: Key: token | Value: {token}
  
    Ejemplo URL: https://siliconaccess.onrender.com/logout/?token={token}
