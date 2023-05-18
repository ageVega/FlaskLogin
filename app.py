from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

if __name__ == '__main__':
    app.run(debug=True)