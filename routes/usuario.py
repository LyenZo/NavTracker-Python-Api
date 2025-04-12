from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controllers.usuarioController import (
    get_all_usuarios, 
    create_usuario, 
    edit_usuario, 
    delete_usuario, 
    login_usuario, 
    get_perfil_usuario  
)

usuario_bp = Blueprint('usuario', __name__)

# -----------------------------------------------------------------------------------------------------
@usuario_bp.route('/', methods=['GET'])
def index():
    user = get_all_usuarios()
    return jsonify(user)

# -----------------------------------------------------------------------------------------------------
@usuario_bp.route('/', methods=['POST'])
def user_store():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        email = data.get('email')
        nombre = data.get('nombre')
        ap_pat = data.get('ap_pat')
        ap_mat = data.get('ap_mat')
        n_tel = data.get('n_tel')
        id_tipo = data.get('id_tipo')
        id_vehiculo = data.get('id_vehiculo')
        password = data.get('password')
        if not nombre or not email:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        print(f"NAME {nombre} --- email {email} --- {password}")
        new_user = create_usuario(nombre, ap_pat, ap_mat, email, password, n_tel, id_tipo, id_vehiculo)
        return jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@usuario_bp.route('/<int:id_u>', methods=['PUT'])
def user_update(id_u):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400

        nombre = data.get('nombre')
        ap_pat = data.get('ap_pat')
        ap_mat = data.get('ap_mat')
        email = data.get('email')
        n_tel = data.get('n_tel')
        id_tipo = data.get('id_tipo')
        id_vehiculo = data.get('id_vehiculo')

        updated_user = edit_usuario(id_u, nombre, ap_pat, ap_mat, email, n_tel, id_tipo, id_vehiculo)
        return jsonify(updated_user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@usuario_bp.route('/<int:id_u>', methods=['DELETE'])
def user_delete(id_u):
    try:
        result = delete_usuario(id_u)
        return jsonify(result), result[1] if isinstance(result, tuple) else 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------------------------------------------------------------------------------
@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_usuario(data.get('email'), data.get('password'))

# -----------------------------------------------------------------------------------------------------
@usuario_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    return get_perfil_usuario()
# -----------------------------------------------------------------------------------------------------
