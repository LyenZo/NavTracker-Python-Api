from flask import Blueprint, jsonify, request
from controllers.rutaController import get_all_rutas, create_ruta, edit_ruta, delete_ruta,get_one_ruta

ruta_bp = Blueprint('ruta', __name__)

@ruta_bp.route('/', methods=['GET'])
def index():
    ruta = get_all_rutas()
    return jsonify(ruta)
#-----------------------------------------------------------------------------------------------------
@ruta_bp.route('/', methods=['POST'])
def ruta_store():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        id_conductor = data.get('id_conductor')
        id_pasajero = data.get('id_pasajero')
        lat_inicio = data.get('lat_inicio')
        lon_inicio = data.get('lon_inicio')
        lat_final = data.get('lat_final')
        lon_final = data.get('lon_final')
        f_inicio = data.get('f_inicio')
        f_final = data.get('f_final')
        distancia = data.get('distancia')
        if not lat_inicio:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        print(f"id_conductor {id_conductor} --- id_pasajero {id_pasajero} --- lat_inicio {lat_inicio} --- lon_inicio {lon_inicio}")
        new_ruta = create_ruta(id_pasajero,id_conductor,lat_inicio,lon_inicio,lat_final,lon_final,f_inicio,f_final,distancia)
        return jsonify(new_ruta), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#-----------------------------------------------------------------------------------------------------
@ruta_bp.route('/<int:id_ruta>', methods=['PUT'])
def user_update(id_ruta):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        id_conductor = data.get('id_conductor')
        id_pasajero = data.get('id_pasajero')
        lat_inicio = data.get('lat_inicio')
        lon_inicio = data.get('lon_inicio')
        lat_final = data.get('lat_final')
        lon_final = data.get('lon_final')
        f_inicio = data.get('f_inicio')
        f_final = data.get('f_final')
        distancia = data.get('distancia')
        updated_ruta = edit_ruta(id_ruta,id_pasajero,id_conductor,lat_inicio,lon_inicio,lat_final,lon_final,f_inicio,f_final,distancia)
        return jsonify(updated_ruta), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@ruta_bp.route('/<int:id_ruta>', methods=['DELETE'])
def ruta_delete(id_ruta):
    try:
        result = delete_ruta(id_ruta)
        return jsonify(result), result[1] if isinstance(result, tuple) else 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# -----------------------------------------------------------------------------------------------------
@ruta_bp.route('/<int:id_ruta>', methods=['GET'])
def ruta_show(id_ruta):
    try:
        ruta = get_one_ruta(id_ruta)
        return jsonify(ruta[0]), ruta[1]  
    except Exception as e:
        return jsonify({"error": str(e)}), 500




