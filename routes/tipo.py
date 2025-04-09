from flask import Blueprint, jsonify, request
from controllers.tipoController import get_all_tipos, create_tipo, edit_tipo, delete_tipo,get_one_tipo

tipo_bp = Blueprint('tipo', __name__)

@tipo_bp.route('/', methods=['GET'])
def index():
    tipo = get_all_tipos()
    return jsonify(tipo)
#-----------------------------------------------------------------------------------------------------
@tipo_bp.route('/', methods=['POST'])
def tipo_store():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        tipo = data.get('tipo')
        if not tipo:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        print(f"NAME {tipo} ")
        new_tipo = create_tipo(tipo)
        return jsonify(new_tipo), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#-----------------------------------------------------------------------------------------------------
@tipo_bp.route('/<int:id_tipo>', methods=['PUT'])
def user_update(id_tipo):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        tipo = data.get('tipo')
        updated_tipo = edit_tipo(id_tipo,tipo)
        return jsonify(updated_tipo), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@tipo_bp.route('/<int:id_tipo>', methods=['DELETE'])
def tipo_delete(id_tipo):
    try:
        result = delete_tipo(id_tipo)
        return jsonify(result), result[1] if isinstance(result, tuple) else 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# -----------------------------------------------------------------------------------------------------
@tipo_bp.route('/<int:id_tipo>', methods=['GET'])
def tipo_show(id_tipo):
    try:
        tipo = get_one_tipo(id_tipo)
        return jsonify(tipo[0]), tipo[1]  
    except Exception as e:
        return jsonify({"error": str(e)}), 500




