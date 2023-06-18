# FlaskLogin

# Instalacion de entorno

## Version de python

### Comprobar version de python y pip

```bash
$ python --version
Python 3.10.4
```

```bash
$ pip --version
pip 22.3.1 from C:\Users\ageve\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```

### Instalar pip

```bash
sudo apt update

sudo apt install python3-pip
```

## Crear entorno virtual

### Instalar y crear virtualenv

```bash
$ pip install virtualenv

$ python -m virtualenv venv
 
$ source venv/Scripts/activate
```

### Instalar dependencias desde requirements.txt

```bash
$ pip install -r requirements.txt
```

### Generar requirements.txt

```bash
$ pip freeze > requirements.txt
```

### Instalar modulos de python en entorno virtual

```bash
$ pip install flask

$ pip install python-dotenv

$ pip install psycopg2 // Libreria para comunicar nuestra aplicacion python con postgres // Instalar postgres o $ sudo apt install libpq-dev

$ pip install flask_login

$ pip install cryptography

$ pip install gunicorn

$ pip install waitress
```