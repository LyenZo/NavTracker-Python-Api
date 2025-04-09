from models.Vehiculo import Vehiculo
from flask import jsonify
from config import db

#----------------------------------------------------------------------------------------------------------------
#GET ALL
def get_all_vehiculos():
    try:
        return[vehiculo.to_dict() for vehiculo in Vehiculo.query.all()]
    except Exception as error:
        print(f"ERROR {error}")
#----------------------------------------------------------------------------------------------------------------
#CREATE
def create_vehiculo(vehiculo):
    try:
        new_vehiculo = Vehiculo(vehiculo)
        db.session.add(new_vehiculo)
        db.session.commit()
        return new_vehiculo.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg' : 'Error al crear vehiculo'}),500
#----------------------------------------------------------------------------------------------------------------
#EDIT
def edit_vehiculo(id_vehiculo, vehiculo=None):
    try:
        vehiculo = Vehiculo.query.get(id_vehiculo)
        if not vehiculo:
            return {"error": "Vehiculo no encontrado"}, 404
        if vehiculo is not None:
            vehiculo.vehiculo = vehiculo
        db.session.commit()
        return vehiculo.to_dict(), 200
    except Exception as e:
        print(f"ERROR: {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#DELETE
def delete_vehiculo(id_vehiculo):
    try:
        vehiculo = Vehiculo.query.get(id_vehiculo)
        if not vehiculo:
            return {"error": "Vehiculo no encontrado"}, 404

        db.session.delete(vehiculo)
        db.session.commit()
        return {"message": "Vehiculo eliminado exitosamente"}, 200
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#GET ONE
def get_one_vehiculo(id_vehiculo):
    try:
        vehiculo = vehiculo.query.get(id_vehiculo) 
        if vehiculo:
            return vehiculo.to_dict(), 200 
        else:
            return {"error": "vehiculo no encontrado"}, 404  
    except Exception as error:
        print(f"ERROR {error}")
        return {"error": str(error)}, 500
#----------------------------------------------------------------------------------------------------------------

