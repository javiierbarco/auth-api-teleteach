# 📜 CHANGELOG

Todas las modificaciones relevantes de este microservicio serán documentadas en este archivo.

Este proyecto sigue la convención de versionado [SemVer](https://semver.org/lang/es/).

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
