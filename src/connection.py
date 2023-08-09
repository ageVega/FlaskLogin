# connection.py
from os import environ
from dotenv import load_dotenv
from psycopg2 import connect, extras

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

def execute_query(query, params):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=extras.RealDictCursor) as cur:
            cur.execute(query, params)
            if cur.description:
                return cur.fetchone()
