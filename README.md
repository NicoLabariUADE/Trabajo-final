# Proyecto Final - CoderHouse
Nicolas Labari Fabressi

## 📂 Funcionalidades principales

- Página de inicio (`/`)
- Página "Acerca de mí" (`/about/`)
- Blog/Páginas en `/pages/` con:
  - Detalle de cada página
  - Crear, editar y eliminar páginas (requiere login)
  - Buscador
- Registro de usuarios (`/accounts/signup/`)
- Login / Logout
- Vista de perfil del usuario
- Edición del perfil (nombre, email, avatar, biografía, etc.)
- Cambio de contraseña

## 👥 Roles de usuario

- Usuarios no registrados: pueden ver las páginas.
- Usuarios registrados: pueden crear, editar, eliminar y gestionar su perfil.

## 🛠 Instalación

1. Cloná el repositorio:
https://github.com/NicoLabariUADE/Trabajo-final.git

2. Crear entorno virtual
python -m venv env
./env/Scripts/activate

3. Instalar dependencias
pip install -r requirements.txt

4. Migracion de DB
python manage.py migrate

5. Ejecutar servidor
Python manage.py runserver

## 📸 Video
