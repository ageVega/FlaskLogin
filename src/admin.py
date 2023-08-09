from .connection import execute_query
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Admin(UserMixin):
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password
        
    def check_password(self, password):
        return check_password_hash(self.password, password)


def get_admin_by_id(admin_id):
    admin_data = execute_query("SELECT * FROM admins WHERE id = %s", (admin_id,))

    if admin_data:
        return Admin(id=admin_data['id'], nickname=admin_data['nickname'], password=admin_data['password'])
    
    return None

def get_admin_by_nickname(nickname):
    admin_data = execute_query("SELECT * FROM admins WHERE nickname = %s", (nickname,))

    if admin_data:
        return Admin(id=admin_data['id'], nickname=admin_data['nickname'], password=admin_data['password'])
    
    return None

def create_admin(nickname, password):
    password_hash = generate_password_hash(password)
    admin_data = execute_query('SELECT * FROM admins WHERE nickname = %s', (nickname,))
    
    if admin_data:
        return None, "Lo sentimos, ese nickname ya está cogido :("
    
    try:
        admin_data = execute_query('INSERT INTO admins (nickname, password) VALUES (%s, %s) RETURNING id, nickname, password', 
                                   (nickname, password_hash))
    except Exception as e:
        return None, str(e)

    return Admin(admin_data['id'], admin_data['nickname'], admin_data['password']), None

def update_password(admin_id, new_password):
    hashed_password = generate_password_hash(new_password)

    try:
        execute_query('UPDATE admins SET password = %s WHERE id = %s', (hashed_password, admin_id))

    except Exception as e:
        print("Error al actualizar la contraseña: ", str(e))
        return False
    
    return True

def delete_admin(admin_id):
    try:
        execute_query("DELETE FROM admins WHERE id = %s", (admin_id,))
        
    except Exception as e:
        print(f"Error deleting admin: {str(e)}")
        return None
