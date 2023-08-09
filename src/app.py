# app.py
from .login import login_manager, admin_blueprint
from os import environ
from dotenv import load_dotenv
from flask import Flask, session, render_template, redirect, url_for
from flask_login import login_required, current_user

load_dotenv()  # Carga las variables de entorno desde .env

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = environ.get('SECRET_KEY')  # Cifra las cookies de sesión del usuario, Flask-Login utiliza estas cookies para recordar a los usuarios entre solicitudes.

app.register_blueprint(admin_blueprint, url_prefix='/auth')

login_manager.init_app(app)
login_manager.login_view = "auth.login"  # Establece la vista de inicio de sesión


@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('home.html')

@app.route('/dashboard')
@login_required
def dashboard():
    admin_nickname = session.get('admin_nickname', '11111111')
    return render_template('dashboard.html', admin_nickname=admin_nickname)

@app.route('/config')
@login_required
def config():
    admin_nickname = session.get('admin_nickname', '11111111')
    return render_template('config.html', admin_nickname=admin_nickname)

@app.route('/change_password')
@login_required
def change_password():
    admin_nickname = session.get('admin_nickname', '11111111')
    return render_template('change_password.html', admin_nickname=admin_nickname)


if __name__ == '__main__':
    env = environ.get('APP_ENV')  
    if env == 'prod':
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    elif env == 'dev':
        app.run(debug=True)
