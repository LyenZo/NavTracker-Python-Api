from flask import Blueprint, jsonify, request
from controllers.puntoController import get_all_puntos, create_punto, edit_punto, delete_punto,get_one_punto

punto_bp = Blueprint('punto', __name__)

@punto_bp.route('/', methods=['GET'])
def index():
    punto = get_all_puntos()
    return jsonify(punto)
#-----------------------------------------------------------------------------------------------------
@punto_bp.route('/', methods=['POST'])
def punto_store():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        nombre = data.get('nombre')
        latitud = data.get('latitud')
        longitud = data.get('longitud')
        direccion = data.get('direccion')
        if not nombre:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        print(f"NAME {nombre} --- latitud {latitud} --- longitud {longitud} --- direccion {direccion}")
        new_punto = create_punto(nombre,latitud,longitud,direccion)
        return jsonify(new_punto), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#-----------------------------------------------------------------------------------------------------
@punto_bp.route('/<int:id_punto>', methods=['PUT'])
def user_update(id_punto):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        nombre = data.get('nombre')
        latitud = data.get('latitud')
        longitud = data.get('longitud')
        direccion = data.get('direccion')
        updated_punto = edit_punto(id_punto,nombre,latitud,longitud,direccion)
        return jsonify(updated_punto), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@punto_bp.route('/<int:id_punto>', methods=['DELETE'])
def punto_delete(id_punto):
    try:
        result = delete_punto(id_punto)
        return jsonify(result), result[1] if isinstance(result, tuple) else 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# -----------------------------------------------------------------------------------------------------
@punto_bp.route('/<int:id_punto>', methods=['GET'])
def punto_show(id_punto):
    try:
        punto = get_one_punto(id_punto)
        return jsonify(punto[0]), punto[1]  
    except Exception as e:
        return jsonify({"error": str(e)}), 500


