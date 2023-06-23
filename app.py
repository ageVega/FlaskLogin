from api import api_blueprint
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix='/api')


@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)