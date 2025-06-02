## Endpoints de Autenticación

Base URL: `/api/auth/`

| Método | Ruta               | Descripción                         | Body / Params                      |
|--------|--------------------|-------------------------------------|------------------------------------|
| POST   | `/register`        | Registro de un nuevo usuario        | `{ "email": "", "password": "" }` |
| POST   | `/login`           | Inicio de sesión                    | `{ "email": "", "password": "" }` |
| POST   | `/logout`          | Cierre de sesión                    | Token en headers                   |
| POST   | `/recover`         | Enviar correo para recuperar clave | `{ "email": "" }`                  |
| POST   | `/reset-password`  | Resetear la contraseña              | `{ "token": "", "new_password": "" }` |

> Todas las respuestas están en formato JSON.
