# admin.py
from .connection import get_connection
from psycopg2 import extras
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

# Definición de la clase usuario
class Admin(UserMixin):
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password
        
    def check_password(self, password):
        return check_password_hash(self.password, password)


# Funcion para conseguir un cursor
def get_cursor():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    return conn, cur

# Funcion para cerrar conexion y cursor
def close_connection_and_cursor(conn, cur):
    cur.close()
    conn.close()

def get_admin_by_id(admin_id):
    conn, cur = get_cursor()
    cur.execute("SELECT * FROM admins WHERE id = %s", (admin_id,))
    admin_data = cur.fetchone()
    close_connection_and_cursor(conn, cur)

    if admin_data:
        return Admin(id=admin_data['id'], nickname=admin_data['nickname'], password=admin_data['password'])
    return None

def get_admin_by_nickname(nickname):
    conn, cur = get_cursor()
    cur.execute("SELECT * FROM admins WHERE nickname = %s", (nickname,))
    admin_data = cur.fetchone()
    close_connection_and_cursor(conn, cur)

    if admin_data:
        return Admin(id=admin_data['id'], nickname=admin_data['nickname'], password=admin_data['password'])
    return None

def create_admin(nickname, password):
    password_hash = generate_password_hash(password)

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    # Primero verificamos si el nickname ya existe
    cur.execute('SELECT * FROM admins WHERE nickname = %s', (nickname,))
    if cur.fetchone():
        return None, "Lo sentimos, ese nickname ya está cogido :("
    
    try:
        cur.execute('INSERT INTO admins (nickname, password) VALUES (%s, %s) RETURNING id, nickname, password', 
                    (nickname, password_hash))
        admin_data = cur.fetchone()
        conn.commit()
    except Exception as e:
        conn.rollback()
        return None, str(e)

    cur.close()
    conn.close()

    return Admin(admin_data['id'], admin_data['nickname'], admin_data['password']), None

def update_password(admin_id, new_password):
    conn = get_connection()
    cur = conn.cursor()

    hashed_password = generate_password_hash(new_password)

    try:
        cur.execute('UPDATE admins SET password = %s WHERE id = %s', (hashed_password, admin_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Error al actualizar la contraseña: ", str(e))
        return False
    finally:
        cur.close()
        conn.close()

    return True

def delete_admin(admin_id):
    conn, cur = get_cursor()

    try:
        cur.execute("DELETE FROM admins WHERE id = %s", (admin_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error deleting admin: {str(e)}")
        return None
    finally:
        close_connection_and_cursor(conn, cur)
