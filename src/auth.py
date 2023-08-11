# login.py
from .connection import get_connection
from psycopg2 import extras
from .admin import get_admin_by_id, get_admin_by_nickname, create_admin, update_password
from flask import Blueprint, request, redirect, url_for, render_template, flash, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

# Crea una instancia de LoginManager, que maneja el proceso de autenticación de usuarios.
login_manager = LoginManager()

@login_manager.user_loader
def load_user(admin_id):
    return get_admin_by_id(admin_id)

admin_blueprint = Blueprint('auth', __name__)


@admin_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nickname = request.form.get('nickname').lower()
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.", "danger")
            return redirect(url_for('auth.register'))

        admin, error = create_admin(nickname, password)
        if error:
            flash(error, "danger")
            return redirect(url_for('auth.register'))

        return redirect(url_for('home'))
    else:
        return render_template('register.html')

@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        nickname = request.form['nickname'].lower()
        password = request.form['password']
        admin = get_admin_by_nickname(nickname)

        if admin:
            if check_password_hash(admin.password, password):
                session['admin_id'] = admin.id
                capitalized_nickname = admin.nickname.capitalize()
                session['admin_nickname'] = capitalized_nickname
                login_user(admin)
                return redirect(url_for('dashboard'))
            else:
                flash('Contraseña incorrecta.')
        else:
            flash('Este admin no existe.')

        return render_template('login.html')
    else:
        return render_template('login.html')

@admin_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@admin_blueprint.route('/change_password', methods=['POST'])
@login_required
def change_password():
    old_password = request.form.get('oldPassword')
    new_password = request.form.get('newPassword')
    confirm_password = request.form.get('confirmPassword')

    if not old_password or not new_password or not confirm_password:
        flash('Por favor, introduce las contraseñas', 'danger')
        return redirect(url_for('change_password'))

    if new_password != confirm_password:
        flash("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.", "danger")
        return redirect(url_for('change_password'))

    admin = get_admin_by_id(current_user.get_id())

    if admin is None:
        flash('Error inesperado. Inténtalo de nuevo.', 'danger')
        return redirect(url_for('change_password'))

    if check_password_hash(admin.password, old_password):
        if old_password == new_password:
            flash('La nueva contraseña debe ser diferente a la antigua', 'danger')
            return redirect(url_for('change_password'))

        hashed_password = generate_password_hash(new_password)
        update_password(admin.id, hashed_password)

        flash('La contraseña ha sido cambiada con éxito', 'success')
        return logout()
    else:
        flash('La contraseña antigua es incorrecta', 'danger')
        return redirect(url_for('change_password'))

@admin_blueprint.route('/confirm_password/<int:admin_id>', methods=['POST'])
@login_required
def confirm_password(admin_id):
    if admin_id != current_user.id:
        return jsonify({'message': 'No puedes confirmar la contraseña de otro administrador'}), 400

    password = request.json.get('password')
    
    admin = get_admin_by_id(admin_id)
    if admin is None:
        return jsonify({'message': 'Este administrador no existe'}), 400

    if not check_password_hash(admin.password, password):
        return jsonify({'message': 'Contraseña incorrecta'}), 400

    return jsonify({'message': 'Contraseña correcta'}), 200

@admin_blueprint.route('/delete/<int:admin_id>', methods=['DELETE'])
@login_required
def delete_admin(admin_id):
    if admin_id != current_user.id:
        return jsonify({'message': 'No puedes eliminar a otro administrador'}), 400

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    try:
        cursor.execute("DELETE FROM admins WHERE id = %s", (admin_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'message': 'Error al eliminar al administrador'}), 500
    finally:
        cursor.close()
        conn.close()

    logout_user()
    return jsonify({'message': 'Admin eliminado correctamente'}), 200
