# login.py
from .connection import get_user_by_id, get_user_by_nickname, create_user, delete_user
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

# Crea una instancia de LoginManager, que maneja el proceso de autenticación de usuarios.
login_manager = LoginManager()

@login_manager.user_loader  # Esto es un decorador que Flask-Login utiliza para cargar un usuario
def load_user(user_id):
    return get_user_by_id(user_id)

# Define un Blueprint para la API. Un Blueprint es un conjunto de rutas que pueden ser registradas en una aplicación Flask.
login_blueprint = Blueprint('auth', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    nickname = request.form.get('username')
    password = request.form.get('password')

    user = get_user_by_nickname(nickname)

    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('home'))

@login_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nickname = request.form.get('username')
        password = request.form.get('password')

        user = get_user_by_nickname(nickname)

        if not user:
            create_user(nickname, password)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    return render_template('register.html')

@login_blueprint.route('/delete', methods=['GET', 'POST'])
@login_required
def delete_account():
    if request.method == 'POST':
        delete_user(current_user.get_id())
        logout_user()
        return redirect(url_for('home'))
    
    return render_template('delete_account.html')
