from jinja2 import Environment, FileSystemLoader
import os

# Configurar el entorno de Jinja2
template_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(template_dir))

# Cargar el template
template = env.get_template('email.cambio.estado.html.j2')

# Datos para renderizar el template
data = {
    'to_name': 'John Doe',
    'token': '1234567890',
    'api_url': 'http://localhost:8000/api/v1/auth/activate_account'
}

# Renderizar el template
rendered_html = template.render(data)

# Guardar el resultado en un archivo HTML
output_file = 'output.html'
with open(output_file, 'w') as f:
    f.write(rendered_html)

print(f'Template renderizado y guardado en {output_file}')
