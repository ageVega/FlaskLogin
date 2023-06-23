import os
from dotenv import load_dotenv
from psycopg2 import connect, extras
from flask import Blueprint, jsonify, request
from flask_login import UserMixin, login_required, current_user

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Accede a las variables de entorno
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')
dbname = os.environ.get('DB_DATABASE')
username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

# Configura la conexión a la base de datos
def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=username, password=password)
    return conn

# Define un Blueprint para la API
api_blueprint = Blueprint('api', __name__)

# Define una clase de modelo para los usuarios
class User(UserMixin):
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password

# Ruta para registrar un nuevo usuario
@api_blueprint.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    nickname = data.get('nickname')
    password = data.get('password')

    if not nickname or not password:
        return jsonify({'error': 'El nickname y la contraseña son obligatorios'}), 400

    # Inserta el nuevo usuario en la base de datos
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO usuarios (nickname, password) VALUES (%s, %s) RETURNING id"
    cursor.execute(query, (nickname, password))
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    # Crea un objeto User y devuelve la información del usuario registrado
    user = User(user_id, nickname, password)
    return jsonify({'id': user.id, 'nickname': user.nickname}), 201

# Ruta para borrar un usuario
@api_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Usuario borrado correctamente'}), 200

# Ruta para obtener todos los usuarios
@api_blueprint.route('/users', methods=['GET'])
@login_required
def get_users():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    query = "SELECT * FROM usuarios"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(users), 200

# Ruta para obtener información del usuario actual
@api_blueprint.route('/users/current', methods=['GET'])
@login_required
def get_current_user():
    user = current_user
    return jsonify({'id': user.id, 'nickname': user.nickname}), 200
