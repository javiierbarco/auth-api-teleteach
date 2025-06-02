# 🔐 TeleTeach – API de Autenticación

Este repositorio contiene el microservicio de autenticación del sistema **TeleTeach**, encargado del registro, inicio de sesión, recuperación de contraseña y gestión de roles para usuarios docentes.

Forma parte del desarrollo del curso **Ingeniería de Software 2 – 2025-1** bajo una arquitectura SOFEA.

---

## 🚀 Tecnologías utilizadas

- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- JWT para autenticación
- Base de datos simulada (JSON o en memoria) para el MVP

---

## ⚙️ Instalación y ejecución local

```bash
# Clona el repositorio
git clone https://github.com/javiierbarco/auth-api-teleteach.git
cd auth-api-teleteach

# Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta el servidor
uvicorn main:app --reload --port 8000
```

---

## 📋 Endpoints principales

| Método | Ruta                          | Función                                 |
|--------|-------------------------------|------------------------------------------|
| POST   | `/api/auth/register`          | Registro de nuevo usuario                |
| POST   | `/api/auth/login`             | Inicio de sesión                         |
| POST   | `/api/auth/logout`            | Cierre de sesión                         |
| POST   | `/api/auth/recover`           | Envío de correo para recuperar contraseña|
| POST   | `/api/auth/reset-password`    | Reestablecer contraseña con token        |

Documentación Swagger disponible en:

```
http://localhost:8000/docs
```

---

## 🔗 Otros Repositorios del Proyecto TeleTeach

- [Frontend TeleTeach](https://github.com/javiierbarco/frontend-teleteach)
- [API de Cursos y Progreso](https://github.com/javiierbarco/courses-api-teleteach)

---

## 👥 Equipo Castores – Ingeniería de Software 2

- Diego H. Lavado G.  
- Estephanie Perez M.  
- Frank S. Pardo A.  
- Javier E. González V.  
- Juan D. Rivera B.  
- Victor M. Torres A.  
- Wullfredo J. Barco G.

---

## 📜 Licencia

Uso académico – Universidad Nacional de Colombia – Ingeniería de Sistemas y Computación – 2025-1
