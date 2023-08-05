# login.py
from .admin import get_admin_by_id, get_admin_by_nickname, create_admin, delete_admin
from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

# Crea una instancia de LoginManager, que maneja el proceso de autenticación de usuarios.
login_manager = LoginManager()

@login_manager.user_loader
def load_user(admin_id):
    return get_admin_by_id(admin_id)

admin_blueprint = Blueprint('auth', __name__)

@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form.get('username')
        password = request.form.get('password')

        admin = get_admin_by_nickname(nickname)

        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('home'))
    return render_template('login.html')

@admin_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@admin_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nickname = request.form.get('username')
        password = request.form.get('password')

        admin = get_admin_by_nickname(nickname)

        if not admin:
            create_admin(nickname, password)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))
    return render_template('register.html')

@admin_blueprint.route('/delete', methods=['GET', 'POST'])
@login_required
def delete_admin():
    if request.method == 'POST':
        delete_admin(current_user.get_id())
        logout_user()
        return redirect(url_for('home'))
    
    return render_template('delete_admin.html')
