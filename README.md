# Guía de Configuración para el Proyecto Django

Este archivo describe los pasos para configurar y ejecutar el proyecto Django.

## 0. Crear entorno virtual

```bash
python -m venv env
```

Activar el entorno virtual

```bash
.\env\Scripts\activate
```

## 1. Instalación de Dependencias

Primero, asegúrate de tener `pip` instalado y actualizado. Luego, instala Django utilizando el siguiente comando:

```bash
pip install django
```

Genera un archivo `requirements.txt` con las dependencias del proyecto:

```bash
pip freeze > requirements.txt
```

Instala las dependencias desde `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 2. Configuración del Proyecto Django

Crea un nuevo proyecto Django llamado `Tienda`:

```bash
django-admin startproject recetas_project
```

Dentro del proyecto, crea una nueva aplicación llamada `recetas_app`:

```bash
django-admin startapp recetas_app
```

## 3. Migraciones

Realiza las migraciones iniciales del proyecto:

```bash
python manage.py migrate
```

Crea las migraciones para la nueva aplicación y actualiza la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 4. Crear un Superusuario

Crea un superusuario para gestionar el panel de administración de Django:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para proporcionar el nombre de usuario, correo electrónico y contraseña.

## 5. Ejecutar el Servidor de Desarrollo

Finalmente, inicia el servidor de desarrollo para ejecutar el proyecto:

```bash
python manage.py runserver
```

Ahora puedes acceder a la aplicación a través de `http://127.0.0.1:8000/` y al panel de administración en `http://127.0.0.1:8000/admin/`.

---

Asegúrate de tener Python y Django instalados correctamente antes de ejecutar estos comandos. Si encuentras algún problema, revisa los mensajes de error para diagnosticar y solucionar el problema.
