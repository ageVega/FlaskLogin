# FlaskLogin

# Instalacion de entorno

## Version de python

- Comprueba la versión de Python y pip con los siguientes comandos:

```bash
$ python --version
Python 3.10.4
```

```bash
$ pip --version
pip 22.3.1 from C:\Users\ageve\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```

- Si Python y pip no están instalados, puedes instalar pip con los siguientes comandos:

```bash
sudo apt update

sudo apt install python3-pip
```

## Crear entorno virtual

- Instala y crea un entorno virtual con los siguientes comandos:

```bash
$ pip install virtualenv

$ python -m virtualenv venv
 
$ source venv/Scripts/activate
```

### Instalar dependencias desde requirements.txt

- Instala las dependencias listadas en el archivo requirements.txt con el siguiente comando:

```bash
$ pip install -r requirements.txt
```

### Generar requirements.txt

- Si necesitas generar un nuevo archivo requirements.txt a partir de las dependencias instaladas en tu entorno virtual, utiliza el siguiente comando:

```bash
$ pip freeze > requirements.txt
```

### Instalar modulos de python en entorno virtual

- Instala los siguientes módulos de Python en tu entorno virtual:

```bash
$ pip install flask

$ pip install python-dotenv

$ pip install psycopg2  # Librería para comunicar nuestra aplicación Python con PostgreSQL. Debes instalar PostgreSQL o ejecutar el siguiente comando: $ sudo apt install libpq-dev

$ pip install flask_login

$ pip install cryptography

$ pip install gunicorn

$ pip install waitress

```

## API

### Obtener todos los usuarios

- Método: `GET`
- Ruta: `/api/users`
- Descripción: Obtiene todos los usuarios registrados en la base de datos.
- Parámetros de autenticación: Se requiere autenticación.
- Respuesta exitosa (JSON):
  - Una lista de objetos de usuario, donde cada objeto contiene:
    - `id` (integer): El ID del usuario.
    - `nickname` (string): El nickname del usuario.
- Código de respuesta exitosa: `200 OK`
- Ejemplo de respuesta:
  ```bash
  HTTP/1.1 200 OK
  Content-Type: application/json

  [
    {
      "id": 1,
      "nickname": "ejemplo"
    },
    {
      "id": 2,
      "nickname": "otro_ejemplo"
    }
  ]

### Obtener información del usuario actual

- Método: `GET`
- Ruta: `/api/users/current`
- Descripción: Obtiene la información del usuario actualmente autenticado.
- Parámetros de autenticación: Se requiere autenticación.
- Respuesta exitosa (JSON):
  - `id` (integer): El ID del usuario actual.
  - `nickname` (string): El nickname del usuario actual.
- Código de respuesta exitosa: `200 OK`
- Ejemplo de respuesta:
  ```bash
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "id": 1,
    "nickname": "ejemplo"
  }

### Registro de usuarios

- Método: `POST`
- Ruta: `/api/users`
- Descripción: Registra un nuevo usuario en la base de datos.
- Parámetros del cuerpo de la solicitud (JSON):
  - `nickname` (string): El nickname del usuario (obligatorio).
  - `password` (string): La contraseña del usuario (obligatorio).
- Respuesta exitosa (JSON):
  - `id` (integer): El ID del usuario registrado.
  - `nickname` (string): El nickname del usuario registrado.
- Código de respuesta exitosa: `201 Created`
- Ejemplo de solicitud:
  ```bash
  POST /api/users
  Content-Type: application/json

  {
    "nickname": "ejemplo",
    "password": "contraseña"
  }

### Borrar un usuario

- Método: `DELETE`
- Ruta: `/api/users/<user_id>`
- Descripción: Borra un usuario de la base de datos.
- Parámetros:
  - `user_id` (integer): El ID del usuario a borrar.
- Parámetros de autenticación: Se requiere autenticación.
- Respuesta exitosa:
  - Código de respuesta exitosa: `200 OK`
