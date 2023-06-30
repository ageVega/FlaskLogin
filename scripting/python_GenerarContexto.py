import os

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content

def write_file_content(output_file, file_name, content):
    output_file.write(f"Content of {file_name}:\n")
    output_file.write(''.join(content))
    output_file.write('\n\n')

def read_specific_files(file_paths, output_path):
    # Asegúrate de que el directorio de salida exista
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    project_root = os.path.join(script_dir, os.pardir)
    
    with open(output_path, 'w') as output_file:
        output_file.write('Estructura del proyecto:\n')
        output_file.write('```\n')
        
        recorded_paths = []
        for file_path in file_paths:
            relative_path = os.path.relpath(file_path, project_root).replace('\\', '/')
            levels = relative_path.split('/')
            for i in range(len(levels)):
                current_path = '/'.join(levels[:i+1])
                if current_path not in recorded_paths:
                    indent = ' ' * 4 * i
                    output_file.write('{}| - {}/\n'.format(indent, levels[i]))
                    recorded_paths.append(current_path)
                    
        output_file.write('```\n\n')
        
        for file_path in file_paths:
            content = read_file_content(file_path)
            relative_path = os.path.relpath(file_path, project_root)
            write_file_content(output_file, relative_path.replace('\\', '/'), content)

# Obtén la ruta del directorio en el que se está ejecutando el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Especifica las rutas de los archivos que quieres leer
file_paths = [
    os.path.join(script_dir, os.pardir, '.env'),
    os.path.join(script_dir, os.pardir, '.gitignore'),
    os.path.join(script_dir, os.pardir, 'requirements.txt'),
    os.path.join(script_dir, os.pardir, 'database.sql'),
    os.path.join(script_dir, os.pardir, 'src', 'app.py'),
    os.path.join(script_dir, os.pardir, 'src', 'user.py'),
    os.path.join(script_dir, os.pardir, 'src', 'connection.py'),
    os.path.join(script_dir, os.pardir, 'src', 'login.py'),
    os.path.join(script_dir, os.pardir, 'tests', 'conftest.py'),
    os.path.join(script_dir, os.pardir, 'tests', 'test_routes.py'),
    os.path.join(script_dir, os.pardir, 'tests', 'test_user_management.py'),
    os.path.join(script_dir, os.pardir, 'templates', 'base.html'),
    os.path.join(script_dir, os.pardir, 'templates', 'home.html'),
    os.path.join(script_dir, os.pardir, 'templates', 'dashboard.html'),
    os.path.join(script_dir, os.pardir, 'templates', 'login.html'),
    os.path.join(script_dir, os.pardir, 'templates', 'register.html'),
    os.path.join(script_dir, os.pardir, 'templates', 'delete_account.html'),
    os.path.join(script_dir, os.pardir, 'static', 'js', 'main.js'),
    os.path.join(script_dir, os.pardir, 'static', 'js', 'dashboard.js'),
    os.path.join(script_dir, os.pardir, 'static', 'css', 'main.css'),
]

# Especifica la ruta de salida
output_path = os.path.join(script_dir, os.pardir, 'tmp', 'context.txt')

read_specific_files(file_paths, output_path)
