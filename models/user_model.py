def validate_user_data(data):
    """
    Verifica que los datos del usuario contengan los campos requeridos.

    Parámetros:
        data (dict): Diccionario con los datos enviados por el usuario (por ejemplo desde un formulario).

    Retorna:
        tuple:
            - True, None si todos los campos requeridos están presentes y no vacíos.
            - False, mensaje de error si falta algún campo o está vacío.
    """
    
    # Define los campos que son obligatorios para el registro de un usuario
    required_fields = ["full_name", "email", "password"]

    # Recorre cada campo obligatorio
    for field in required_fields:
        # Verifica que el campo exista en los datos y que no esté vacío o contenga solo espacios
        if field not in data or not data[field].strip():
            # Si falta el campo o está vacío, devuelve False con un mensaje de error personalizado
            return False, f"El campo '{field}' es obligatorio."

    # Si todos los campos están presentes y válidos, devuelve True y None (sin mensaje de error)
    return True, None
