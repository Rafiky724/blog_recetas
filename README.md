# 🥗 Blog de Recetas - Proyecto Django

Este proyecto es una aplicación web construida con **Django** que permite a los usuarios **añadir, puntuar y comentar recetas**.  
Cada usuario puede crear su cuenta, compartir sus propias recetas y participar en la comunidad calificando y dejando opiniones sobre las recetas de otros.

---

## ⚙️ 1. Configuración del Entorno

Crea y activa un entorno virtual (recomendado):

```bash
python -m venv env
.\env\Scriptsctivate
```

> 💡 En Linux/MacOS: `source env/bin/activate`

---

## 📦 2. Instalación de Dependencias

Instala las dependencias necesarias del proyecto:

```bash
pip install -r requirements.txt
```

Si aún no tienes el archivo `requirements.txt`, puedes generarlo con:

```bash
pip freeze > requirements.txt
```

## 🚀 3. Ejecutar el Servidor de Desarrollo

Inicia el servidor local con:

```bash
python manage.py runserver
```

Accede al sitio en:  
👉 `http://127.0.0.1:8000/`  

---

## 🧩 4. Funcionalidades Principales

- 👨‍🍳 **Gestión de Recetas**: los usuarios pueden crear, editar y eliminar sus recetas.  
- ⭐ **Puntuación**: cada receta puede recibir calificaciones de otros usuarios.  
- 💬 **Comentarios**: los usuarios pueden dejar opiniones en las recetas.  
- 🔐 **Autenticación**: registro, inicio y cierre de sesión de usuarios.  
- 📷 **Multimedia**: soporte para imágenes en las recetas.  

---

## 🧰 5. Tecnologías Utilizadas

- **Python 3.x**
- **Django 5.x**
- **SQLite3**
- **HTML / CSS / Bootstrap** (para la interfaz básica)

---

## 📄 Licencia

Este proyecto es de uso educativo y libre bajo la licencia **MIT**.  
Puedes modificarlo y distribuirlo libremente con atribución al autor original.

---