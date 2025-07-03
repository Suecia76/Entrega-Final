# Entrega-Final

Este proyecto es una aplicación web desarrollada con Django que permite a los usuarios registrarse, iniciar sesión, crear, editar y eliminar libros, así como gestionar su perfil y avatar.

## Requisitos

- Python 3.10 o superior
- pip
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (opcional pero recomendado)

## Instalación

1. **Clona el repositorio:**

   ```sh
   git clone https://github.com/Suecia76/Entrega-Final.git
   cd Entrega-Final/entregafinal
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```sh
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones de la base de datos:**

   ```sh
   python manage.py migrate
   ```

5. **Crea un superusuario (opcional, para acceder al admin):**

   ```sh
   python manage.py createsuperuser
   ```

6. **Inicia el servidor de desarrollo:**

   ```sh
   python manage.py runserver
   ```

7. **Accede a la aplicación:**

   Abre tu navegador y entra a [http://localhost:8000](http://localhost:8000)

## Funcionalidades

- Registro y autenticación de usuarios.
- Gestión de perfil y avatar.
- CRUD de libros (crear, ver, editar, borrar).
- Panel de administración de Django.
- Subida de imágenes para libros y avatares.
- Página de "Sobre mí".

## Estructura de carpetas principal

- `blog/`: Lógica y vistas para la gestión de libros.
- `usuarios/`: Lógica y vistas para usuarios y perfiles.
- `templates/`: Archivos HTML.
- `static/`: Archivos estáticos (CSS, imágenes).
- `media/`: Archivos subidos por los usuarios (imágenes de libros y avatares).

## Notas

- Los archivos subidos se guardan en la carpeta `media/`.
- Para producción, recuerda configurar correctamente las variables de entorno y el manejo de archivos estáticos y media.
- Link del video explicativo: [https://www.youtube.com/watch?v=KgVLAKqeTEE]

---

¡Listo! Ahora puedes comenzar a usar la aplicación.