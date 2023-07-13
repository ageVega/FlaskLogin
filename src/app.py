# app.py
from .login import login_manager, user_management_blueprint
from os import environ
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_login import login_required, current_user

load_dotenv()  # Carga las variables de entorno desde .env

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = environ.get('SECRET_KEY')  # Se utiliza para cifrar las cookies de sesión del usuario, Flask-Login utiliza estas cookies para recordar a los usuarios entre solicitudes.

app.register_blueprint(user_management_blueprint, url_prefix='/auth')

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
    return render_template('dashboard.html', user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
