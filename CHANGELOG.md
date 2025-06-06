# 📜 CHANGELOG

Todas las modificaciones relevantes de este microservicio serán documentadas en este archivo.

Este proyecto sigue la convención de versionado [SemVer](https://semver.org/lang/es/).

---

## [0.1.2] - 2025-06-06
### Agregado
- Ruta `/register` con validación de campos requeridos (`full_name`, `email`, `password`).
- Ruta `/login` con verificación segura usando `werkzeug.security`.
- Validación básica y respuestas JSON claras para login y registro.
- Archivo `.env` soportado con variable `MONGO_URI`.

### Mejorado
- Estructura del proyecto modularizada: `core/`, `models/`, `routes/`, `utils/`.
- Separación de lógica: validación (`user_model.py`), seguridad (`security.py`) y conexión Mongo (`db.py`).
- Manejo de errores con `err?.response?.data?.msg` desde el frontend.

### Corregido
- Error de importación `ModuleNotFoundError: No module named 'core.db'` resuelto con `sys.path.insert` en `app.py`.
- Errores de frontend al registrar corregidos por falta de manejo de `err.response`.

---

## [0.1.1] - 2025-06-02
### Corregido
- Manejo de tokens JWT expirados: ahora se responde con un mensaje claro y código 401 cuando el token está vencido.
- Respuesta de error mejorada para rutas protegidas sin token válido.

### Cambiado
- Validación de contraseñas reforzada: se exige al menos 8 caracteres, una letra mayúscula, una minúscula y un número.
- Se aplicó limpieza de imports y simplificación en el esquema de respuestas de autenticación.

---

## [0.1.0] - 2025-06-02
### Agregado
- Estructura base del microservicio creada con FastAPI.
- Endpoints definidos: registro, login, logout, recuperación y reseteo de contraseña.
- Documentación Swagger habilitada en `/docs`.
- Variables de entorno iniciales documentadas.
- Integración local con frontend y cursos-api simulada.
