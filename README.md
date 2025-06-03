# 🔐 TeleTeach – API de Autenticación

Este repositorio contiene el microservicio de autenticación del sistema **TeleTeach**, encargado del registro, inicio de sesión, recuperación de contraseña, validación de sesiones y gestión de roles para usuarios docentes.

Forma parte del desarrollo del curso **Ingeniería de Software 2 – 2025-1** bajo una arquitectura SOFEA con microservicios RESTful.

---

## 🚀 Tecnologías utilizadas

- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- JWT (JSON Web Tokens) para autenticación y autorización
- Almacenamiento simulado con estructura JSON en memoria (MVP)
- Manejo de variables de entorno con `python-dotenv`

---

## ⚙️ Instalación y ejecución local

""ash""
# Clona el repositorio
git clone https://github.com/javiierbarco/auth-api-teleteach.git
cd auth-api-teleteach

# Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el servidor
uvicorn app.main:app --reload --port 8000

📋 Endpoints principales 

| Método | Ruta                       | Funcionalidad                                                   |
| ------ | -------------------------- | --------------------------------------------------------------- |
| POST   | `/api/auth/register`       | Registro de nuevo usuario (docente)                             |
| POST   | `/api/auth/login`          | Inicio de sesión y generación de token JWT                      |
| POST   | `/api/auth/logout`         | Cierre de sesión local (simulado)                               |
| POST   | `/api/auth/recover`        | Solicitud de recuperación de contraseña                         |
| POST   | `/api/auth/reset-password` | Reestablecer contraseña con token enviado por correo (simulado) |
| GET    | `/api/auth/me`             | Verifica y retorna los datos del usuario autenticado (token)    |


📄 Documentación Swagger generada automáticamente: http://localhost:8000/docs

🛡️ Validaciones y seguridad
Contraseñas seguras: mínimo 8 caracteres, una mayúscula, una minúscula y un número.

JWT tokens: duración configurable vía .env, verificación integrada en rutas protegidas.

Manejo de expiración: respuesta 401 Unauthorized clara cuando el token ha expirado.

🔗 Otros Repositorios del Proyecto TeleTeach
📦 Frontend TeleTeach

📘 API de Cursos y Progreso

👥 Equipo Castores – Ingeniería de Software 2
Diego H. Lavado G.

Estephanie Perez M.

Frank S. Pardo A.

Javier E. González V.

Juan D. Rivera B.

Victor M. Torres A.

Wullfredo J. Barco G.
