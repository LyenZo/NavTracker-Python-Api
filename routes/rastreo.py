from flask import Blueprint, jsonify, request
from controllers.rastreoController import get_all_rastreos, create_rastreo, edit_rastreo, delete_rastreo,get_one_rastreo

rastreo_bp = Blueprint('rastreo', __name__)

@rastreo_bp.route('/', methods=['GET'])
def index():
    rastreos = get_all_rastreos()
    return jsonify(rastreos)
#-----------------------------------------------------------------------------------------------------
@rastreo_bp.route('/', methods=['POST'])
def rastreo_store():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        lng = data.get('lng')
        lat = data.get('lat')
        altitud = data.get('altitud')
        velocidad = data.get('velocidad')
        hora = data.get('hora')
        fecha = data.get('fecha')
        if not lng:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        print(f"NAME --- latitud {lat} --- longitud {lng} --- direccion {altitud}")
        new_rastreo = create_rastreo(lat,lng,altitud,velocidad,hora,fecha)
        return jsonify(new_rastreo), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#-----------------------------------------------------------------------------------------------------
@rastreo_bp.route('/<int:id_rastreo>', methods=['PUT'])
def rastreo_update(id_rastreo):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        lng = data.get('lng')
        lat = data.get('lat')
        altitud = data.get('altitud')
        velocidad = data.get('velocidad')
        hora = data.get('hora')
        fecha = data.get('fecha')
        updated_rastreo = edit_rastreo(id_rastreo,lat,lng,altitud,velocidad,hora,fecha)
        return jsonify(updated_rastreo), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@rastreo_bp.route('/<int:id_rastreo>', methods=['DELETE'])
def rastreo_delete(id_rastreo):
    try:
        result = delete_rastreo(id_rastreo)
        return jsonify(result), result[1] if isinstance(result, tuple) else 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# -----------------------------------------------------------------------------------------------------
@rastreo_bp.route('/<int:id_rastreo>', methods=['GET'])
def rastreo_show(id_rastreo):
    try:
        rastreo = get_one_rastreo(id_rastreo)
        return jsonify(rastreo[0]), rastreo[1]  
    except Exception as e:
        return jsonify({"error": str(e)}), 500




