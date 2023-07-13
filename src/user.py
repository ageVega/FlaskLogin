# user.py
from .connection import get_connection
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

# Definición de la clase usuario
class User(UserMixin):
    def __init__(self, id, nickname, password_hash):
        self.id = id
        self.nickname = nickname
        self.password_hash = password_hash
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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
