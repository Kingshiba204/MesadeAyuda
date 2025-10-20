ProyectoMesa — Mesa de Ayuda

Requisitos
Python 3.10+
Virtualenv o venv
Git
Instalación rápida (Windows PowerShell)
Clona el repositorio y ve al directorio del proyecto:
git clone < https://github.com/Kingshiba204/MesadeAyuda/pull/new/master> & cd ProyectoMesa

Crea y activa un entorno virtual (PowerShell):
python -m venv .venv
..venv\Scripts\Activate.ps1

Instala dependencias:
pip install -r requirements.txt

Crea el archivo de entorno a partir del ejemplo:
Copy-Item .env.example .env

Aplica las migraciones:
python manage.py migrate

Ejecuta el servidor de desarrollo:
python manage.py runserver

Configuración de variables de entorno
Usa .env para variables sensibles y locales. Aquí tienes un ejemplo mínimo en la sección siguiente.

Variables comunes:
DJANGO_SECRET_KEY: clave secreta de Django.
DEBUG: True/False.
ALLOWED_HOSTS: hosts permitidos separados por comas.
DATABASE_ENGINE, DATABASE_NAME: (si usas SQLite por defecto no es estrictamente necesario cambiar).
USUARIO_DEMO_USERNAME, USUARIO_DEMO_EMAIL, USUARIO_DEMO_PASSWORD: valores para el usuario demo (si usas el comando create_demo_user).
.env.example (ejemplo)
DJANGO_SECRET_KEY=replace-this-with-a-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

Base de datos:
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

Usuarios demo
En este proyecto hay dos usuarios de demostración (credenciales proporcionadas):
Super User
Usuario: paciente-0
Contraseña: cachantun

Usuario: usuario_normal
Contraseña: Secreto123

Cómo usar los usuarios demo
Accede a la página de login de la aplicación (habitualmente en /accounts/login/ o la ruta que defina ProyectoMesa).
Introduce el nombre de usuario y la contraseña de uno de los usuarios de demo anteriores.
Crear los usuarios manualmente (si no existen)
Si necesitas crear estas cuentas manualmente en una instalación nueva, abre el shell de Django:
python manage.py shell
Y ejecuta:
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_user('paciente-0', email='paciente0@gmail.com', password='cachantun')
User.objects.create_user('usuario_normal', email='usuario_normal@gmail.com', password='Secreto123')
O, si prefieres automatizarlo, puedo generar un comando de management create_demo_users que cree ambos usuarios automáticamente.

Notas importantes
No uses estas cuentas ni sus contraseñas en producción. Son únicamente para pruebas locales o demos.
Si tu app usa is_staff o permisos especiales para acceder al admin, revisa los flags de usuario (is_staff, is_superuser) y ajústalos si necesitas acceso al panel de administración.
Asegúrate de no commitear el archivo .env.

Notas sobre migraciones
Las migraciones del app Mesa_de_Ayuda deben estar incluidas en Mesa_de_Ayuda/migrations/. Antes de ejecutar el servidor en un entorno nuevo, asegúrate de:
ejecutar python manage.py migrate para aplicar migraciones, si generas nuevas migraciones, usa python manage.py makemigrations y verifica los cambios.
