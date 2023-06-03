import os
from dotenv import load_dotenv
from psycopg2 import connect

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # Aquí se carga la URL de la base de datos desde las variables de entorno

conn = connect(DATABASE_URL)
