🚀 ProyectoMesa — Mesa de Ayuda
Este documento proporciona las instrucciones necesarias para la instalación, configuración y ejecución del proyecto de Mesa de Ayuda.

📋 Requisitos Previos
Asegúrate de tener instalado el siguiente software en tu sistema:
Python 3.10+
Git
Entorno virtual (se recomienda venv o virtualenv)

⚙️ Instalación Rápida (Windows PowerShell)
Sigue estos pasos para poner en marcha el proyecto en un entorno de desarrollo local.

Clona el repositorio y navega al directorio del proyecto: (Nota: La URL del repositorio ha sido corregida; la original era un enlace a un Pull Request).

PowerShell
git clone https://github.com/Kingshiba204/MesadeAyuda.git
cd ProyectoMesa
Crea y activa un entorno virtual (usando PowerShell):

PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
Instala las dependencias del proyecto:

PowerShell

pip install -r requirements.txt
Crea el archivo de entorno a partir del ejemplo:

PowerShell
Copy-Item .env.example .env
(Deberás editar el archivo .env recién creado con tu configuración específica, como se detalla en la siguiente sección).

Aplica las migraciones de la base de datos:

PowerShell
python manage.py migrate
Ejecuta el servidor de desarrollo:

PowerShell
python manage.py runserver
La aplicación estará disponible en http://127.0.0.1:8000/.

🔧 Configuración de Variables de Entorno
El archivo .env se utiliza para gestionar variables sensibles y configuraciones locales sin exponerlas en el control de versiones.

Variables Comunes
DJANGO_SECRET_KEY: Clave secreta única para la instancia de Django.

DEBUG: True para modo desarrollo, False para producción.

ALLOWED_HOSTS: Hosts/dominios permitidos separados por comas (ej. 127.0.0.1,localhost).

USUARIO_DEMO_USERNAME, USUARIO_DEMO_EMAIL, USUARIO_DEMO_PASSWORD: Credenciales para comandos de creación de usuarios demo (si se implementan).

Ejemplo (.env.example)
Este es un ejemplo básico de la configuración requerida en tu archivo .env.
Ini, TOML

# Configuración Central de Django
# REEMPLAZA ESTO con una clave secreta generada
DJANGO_SECRET_KEY=replace-this-with-a-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Base de datos (Default SQLite)
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

👨‍💻 Usuarios de Demostración
El proyecto puede incluir (o puedes crear) usuarios de demostración para facilitar las pruebas.

Credenciales de Acceso
Super Usuario:
Usuario: paciente-0
Contraseña: cachantun

Usuario Normal:
Usuario: usuario_normal
Contraseña: Secreto123

Creación Manual (Si no existen)
Si estás en una instalación nueva y los usuarios no existen, puedes crearlos manualmente:

Abre el shell interactivo de Django:

PowerShell
python manage.py shell
Ejecuta el siguiente script de Python dentro del shell:

Python
from django.contrib.auth import get_user_model
User = get_user_model()

# Crear Super Usuario (si no existe)
if not User.objects.filter(username='paciente-0').exists():
    User.objects.create_superuser('paciente-0', 'paciente0@gmail.com', 'cachantun')
    print("Super usuario 'paciente-0' creado exitosamente.")

# Crear Usuario Normal (si no existe)
if not User.objects.filter(username='usuario_normal').exists():
    User.objects.create_user('usuario_normal', 'usuario_normal@gmail.com', 'Secreto123')
    print("Usuario 'usuario_normal' creado exitosamente.")

exit()
⚠️ Notas Importantes
Seguridad
No uses las credenciales de demostración ni claves secretas de ejemplo en un entorno de producción.

Asegúrate de que tu archivo .env esté listado en .gitignore y nunca se suba al repositorio.

Migraciones
Las migraciones para la aplicación principal se encuentran en Mesa_de_Ayuda/migrations/.

Ejecuta siempre python manage.py migrate después de clonar el repositorio o cambiar de rama.

Si realizas cambios en los modelos (models.py), debes generar nuevas migraciones con python manage.py makemigrations.
