from models.Tipo import Tipo
from flask import jsonify
from config import db

#----------------------------------------------------------------------------------------------------------------
#GET ALL
def get_all_tipos():
    try:
        return[tipo.to_dict() for tipo in Tipo.query.all()]
    except Exception as error:
        print(f"ERROR {error}")
#----------------------------------------------------------------------------------------------------------------
#CREATE
def create_tipo(tipo):
    try:
        new_tipo = Tipo(tipo)
        db.session.add(new_tipo)
        db.session.commit()
        return new_tipo.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg' : 'Error al crear tipo'}),500
#----------------------------------------------------------------------------------------------------------------
#EDIT
def edit_tipo(id_tipo, tipo=None):
    try:
        tipo = Tipo.query.get(id_tipo)
        if not tipo:
            return {"error": "Tipo no encontrado"}, 404
        if tipo is not None:
            tipo.tipo = tipo
        db.session.commit()
        return tipo.to_dict(), 200
    except Exception as e:
        print(f"ERROR: {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#DELETE
def delete_tipo(id_tipo):
    try:
        tipo = Tipo.query.get(id_tipo)
        if not tipo:
            return {"error": "Tipo no encontrado"}, 404

        db.session.delete(tipo)
        db.session.commit()
        return {"message": "Tipo eliminado exitosamente"}, 200
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#GET ONE
def get_one_tipo(id_tipo):
    try:
        tipo = Tipo.query.get(id_tipo) 
        if tipo:
            return tipo.to_dict(), 200 
        else:
            return {"error": "Tipo no encontrado"}, 404  
    except Exception as error:
        print(f"ERROR {error}")
        return {"error": str(error)}, 500
#----------------------------------------------------------------------------------------------------------------

