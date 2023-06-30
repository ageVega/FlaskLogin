# Las pruebas de las rutas Flask. Aquí probamos si las rutas están devolviendo las respuestas y los códigos de estado esperados.
def test_index(client):
    response = client.get('/')
    assert response.status_code == 302  # Espera una redirección al home

def test_home(client):
    response = client.get('/home')
    assert response.status_code == 200  # Espera una respuesta exitosa

def test_dashboard(client):
    response = client.get('/dashboard')
    assert response.status_code == 302  # Espera una redirección debido a que el usuario no está autenticado
