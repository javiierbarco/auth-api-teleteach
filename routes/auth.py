from flask import Blueprint, request, jsonify
from core.db import db  # Conexión a la base de datos MongoDB
from models.user_model import validate_user_data  # Validación de datos del usuario
from utils.security import hash_password, verify_password  # Funciones para manejo seguro de contraseñas

# Crea un blueprint para el módulo de autenticación
auth_bp = Blueprint("auth", __name__)

# Accede a la colección 'users' de la base de datos
users_collection = db["users"]

# Ruta para registrar nuevos usuarios
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json  # Obtiene los datos enviados en formato JSON

    # Valida que todos los campos requeridos estén presentes y no vacíos
    valid, error = validate_user_data(data)
    if not valid:
        return jsonify({"msg": error}), 400  # Si hay error, responde con mensaje y código 400

    # Verifica si ya existe un usuario con ese correo
    if users_collection.find_one({"email": data["email"]}):
        return jsonify({"msg": "El correo ya está registrado"}), 400

    # Hashea la contraseña antes de guardarla
    hashed_pw = hash_password(data["password"])

    # Inserta el nuevo usuario en la base de datos
    users_collection.insert_one({
        "full_name": data["full_name"],
        "email": data["email"],
        "password": hashed_pw
    })

    # Respuesta exitosa
    return jsonify({"msg": "Usuario registrado exitosamente"}), 201

# Ruta para iniciar sesión
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json  # Obtiene los datos enviados en formato JSON

    # Verifica que se hayan enviado el email y la contraseña
    if not data.get("email") or not data.get("password"):
        return jsonify({"msg": "Correo y contraseña son requeridos"}), 400

    # Busca el usuario por email en la base de datos
    user = users_collection.find_one({"email": data["email"]})

    # Verifica que el usuario exista y que la contraseña coincida (usando hash)
    if not user or not verify_password(data["password"], user["password"]):
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    # Si todo está correcto, retorna los datos del usuario (excepto la contraseña)
    return jsonify({
        "msg": "Inicio de sesión exitoso",
        "user": {
            "full_name": user["full_name"],
            "email": user["email"]
        }
    }), 200

# Ruta para eliminar un usuario por su email (útil para pruebas)
@auth_bp.route("/delete_user", methods=["DELETE"])
def delete_user():
    email = request.args.get("email")

    if not email:
        return jsonify({"msg": "Falta el parámetro 'email'"}), 400

    result = users_collection.delete_one({"email": email})

    if result.deleted_count == 0:
        return jsonify({"msg": "No se encontró ningún usuario con ese correo"}), 404

    return jsonify({"msg": f"Usuario con correo {email} eliminado"}), 200


@auth_bp.route('/error')
def error():
    return "Algo falló", 500