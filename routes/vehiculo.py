from flask import Blueprint, jsonify, request
from controllers.vehiculoController import get_all_vehiculos, create_vehiculo, edit_vehiculo, delete_vehiculo,get_one_vehiculo

vehiculo_bp = Blueprint('vehiculo', __name__)

@vehiculo_bp.route('/', methods=['GET'])
def index():
    vehiculo = get_all_vehiculos()
    return jsonify(vehiculo)
#-----------------------------------------------------------------------------------------------------
@vehiculo_bp.route('/', methods=['POST'])
def vehiculo_store():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        vehiculo = data.get('vehiculo')
        if not vehiculo:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        print(f"NAME {vehiculo} ")
        new_vehiculo = create_vehiculo(vehiculo)
        return jsonify(new_vehiculo), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#-----------------------------------------------------------------------------------------------------
@vehiculo_bp.route('/<int:id_vehiculo>', methods=['PUT'])
def user_update(id_vehiculo):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        vehiculo = data.get('vehiculo')
        updated_vehiculo = edit_vehiculo(id_vehiculo,vehiculo)
        return jsonify(updated_vehiculo), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@vehiculo_bp.route('/<int:id_vehiculo>', methods=['DELETE'])
def vehiculo_delete(id_vehiculo):
    try:
        result = delete_vehiculo(id_vehiculo)
        return jsonify(result), result[1] if isinstance(result, tuple) else 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# -----------------------------------------------------------------------------------------------------
@vehiculo_bp.route('/<int:id_vehiculo>', methods=['GET'])
def vehiculo_show(id_vehiculo):
    try:
        vehiculo = get_one_vehiculo(id_vehiculo)
        return jsonify(vehiculo[0]), vehiculo[1]  
    except Exception as e:
        return jsonify({"error": str(e)}), 500




