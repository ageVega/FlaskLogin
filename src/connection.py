# connection.py
from .user import User
from os import environ
from dotenv import load_dotenv
from psycopg2 import connect
from werkzeug.security import generate_password_hash

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Accede a las variables de entorno
host = environ.get('DB_HOST')
port = environ.get('DB_PORT')
dbname = environ.get('DB_DATABASE')
username = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')

# Configura la conexión a la base de datos
def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=username, password=password)
    return conn

def get_user_by_id(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()

    if user_data:
        return User(id=user_data[0], nickname=user_data[1], password_hash=user_data[2])
    return None

def get_user_by_nickname(nickname):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE nickname = %s", (nickname,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()

    if user_data:
        return User(id=user_data[0], nickname=user_data[1], password_hash=user_data[2])
    return None

def create_user(nickname, password):
    conn = get_connection()
    cur = conn.cursor()
    password_hash = generate_password_hash(password)
    cur.execute("INSERT INTO usuarios (nickname, password) VALUES (%s, %s)", (nickname, password_hash))
    conn.commit()
    cur.close()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
