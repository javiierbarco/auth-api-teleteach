import sys
import os

#  Asegura que Python trate este directorio como raíz para imports como core.db
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Obtiene la ruta absoluta del directorio actual
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)  # Inserta esa ruta al inicio del sys.path para que los imports funcionen correctamente

#  Importa Flask y CORS para crear y exponer la API
from flask import Flask
from flask_cors import CORS

#  Importa las rutas definidas para autenticación (registro, login)
from routes.auth import auth_bp

#  Crea la aplicación Flask
app = Flask(__name__)

#  Habilita CORS para permitir solicitudes desde el frontend
CORS(app)

#  Registra el blueprint que maneja las rutas de autenticación
app.register_blueprint(auth_bp)

# Ejecuta la aplicación si se corre directamente con `python app.py`
if __name__ == "__main__":
    app.run(debug=True)  # El modo debug permite ver errores en tiempo real (no usar en producción)
