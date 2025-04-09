from models.Usuario import Usuario
from flask import jsonify
from config import db
from flask_jwt_extended import create_access_token  

#----------------------------------------------------------------------------------------------------------------
#GET ALL
def get_all_usuarios():
    try:
        return[usuario.to_dict() for usuario in Usuario.query.all()]
    except Exception as error:
        print(f"ERROR {error}")
#----------------------------------------------------------------------------------------------------------------
#CREATE
def create_usuario(nombre,ap_pat,ap_mat,email,password,n_tel,id_tipo,id_vehiculo):
    try:
        new_usuario = Usuario(nombre,ap_pat,ap_mat,email,password,n_tel,id_tipo,id_vehiculo)
        db.session.add(new_usuario)
        db.session.commit()
        return new_usuario.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg' : 'Error al crear usuario'}),500
#----------------------------------------------------------------------------------------------------------------
#EDIT
def edit_usuario(id_u, nombre=None, ap_pat=None, ap_mat=None, email=None, n_tel=None, id_tipo=None, id_vehiculo=None):
    try:
        user = Usuario.query.get(id_u)
        if not user:
            return {"error": "Usuario no encontrado"}, 404
        if nombre is not None:
            user.nombre = nombre
        if ap_pat is not None:
            user.ap_pat = ap_pat
        if ap_mat is not None:
            user.ap_mat = ap_mat
        if email is not None:
            user.email = email
        if n_tel is not None:
            user.n_tel = n_tel
        if id_tipo is not None:
            user.id_tipo = id_tipo
        if id_vehiculo is not None:
            user.id_vehiculo = id_vehiculo
        db.session.commit()
        return user.to_dict(), 200
    except Exception as e:
        print(f"ERROR: {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#DELETE
def delete_usuario(id_u):
    try:
        usuario = Usuario.query.get(id_u)
        if not usuario:
            return {"error": "Usuario no encontrado"}, 404

        db.session.delete(usuario)
        db.session.commit()
        return {"message": "Usuario eliminado exitosamente"}, 200
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#LOGIN
def login_usuario(email, password):
    usuario = Usuario.query.filter_by(email=email).first();
    if usuario and usuario.check_password(password):
            access_token = create_access_token(identity=usuario.id_u);
            return jsonify ( {
                'access_token': access_token,
                'usuario': {
                    "id": usuario.id_u,
                    "nombre": usuario.nombre,
                    "email": usuario.email
                }
        })
    return jsonify({"msg":"Credenciales invalidas"}),401