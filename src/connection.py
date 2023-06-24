#connection.py
from .user import User
from os import environ
from dotenv import load_dotenv
from psycopg2 import connect

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

def get_nickname_by_id(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()

    if user_data:
        return User(id=user_data[0], nickname=user_data[1], password=user_data[2])
    
    return None