# admin.py
from .connection import get_connection
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

# Definición de la clase usuario
class Admin(UserMixin):
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


def get_admin_by_id(admin_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admins WHERE id = %s", (admin_id,))
    admin_data = cur.fetchone()
    cur.close()
    conn.close()

    if admin_data:
        return Admin(id=admin_data[0], nickname=admin_data[1], password_hash=admin_data[2])
    return None

def get_admin_by_nickname(nickname):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admins WHERE nickname = %s", (nickname,))
    admin_data = cur.fetchone()
    cur.close()
    conn.close()

    if admin_data:
        return Admin(id=admin_data[0], nickname=admin_data[1], password_hash=admin_data[2])
    return None

def create_admin(nickname, password):
    conn = get_connection()
    cur = conn.cursor()
    password_hash = generate_password_hash(password)
    cur.execute("INSERT INTO admins (nickname, password) VALUES (%s, %s)", (nickname, password_hash))
    conn.commit()
    cur.close()
    conn.close()

def delete_admin(admin_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM admins WHERE id = %s", (admin_id,))
    conn.commit()
    cur.close()
    conn.close()
