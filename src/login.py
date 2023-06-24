#login.py
from .user import User
from .connection import get_connection, get_nickname_by_id
from flask import Blueprint
from flask_login import LoginManager, UserMixin

# Define un Blueprint para la API. Un Blueprint es un conjunto de rutas que pueden ser registradas en una aplicación Flask.
login_blueprint = Blueprint('login', __name__)

# Crea una instancia de LoginManager, que maneja el proceso de autenticación de usuarios.
login_manager = LoginManager()

@login_manager.user_loader  # Esto es un decorador que Flask-Login utiliza para cargar un usuario
def load_user(user_id):
    return get_nickname_by_id(user_id)
