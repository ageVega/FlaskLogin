#login.py
from flask import Blueprint
from flask_login import LoginManager, UserMixin

# Define un Blueprint para la API. Un Blueprint es un conjunto de rutas que pueden ser registradas en una aplicación Flask.
login_blueprint = Blueprint('login', __name__)

# Crea una instancia de LoginManager, que maneja el proceso de autenticación de usuarios.
login_manager = LoginManager()

# Define una clase de modelo para los usuarios
class User(UserMixin):
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password

# Ruta para registrar un nuevo usuario

# Ruta para borrar un usuario

# Ruta para obtener todos los usuarios

# Ruta para obtener información del usuario actual
