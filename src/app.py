# app.py
from os import environ
from .login import login_manager, user_management_blueprint
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_login import login_required, current_user

load_dotenv()  # Carga las variables de entorno desde .env

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = environ.get('SECRET_KEY')  # Necesario para flask-login

app.register_blueprint(user_management_blueprint, url_prefix='/auth')

login_manager.init_app(app)
login_manager.login_view = "auth.login"  # Establece la vista de inicio de sesión


@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dashboard')
@login_required  # Solo los usuarios autenticados pueden acceder al tablero
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
