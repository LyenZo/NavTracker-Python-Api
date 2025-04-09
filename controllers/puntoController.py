from models.Punto import Punto
from flask import jsonify
from config import db

#----------------------------------------------------------------------------------------------------------------
#GET ALL
def get_all_puntos():
    try:
        return[punto.to_dict() for punto in Punto.query.all()]
    except Exception as error:
        print(f"ERROR {error}")
#----------------------------------------------------------------------------------------------------------------
#CREATE
def create_punto(nombre,latitud,longitud,direccion):
    try:
        new_punto = Punto(nombre,latitud,longitud,direccion)
        db.session.add(new_punto)
        db.session.commit()
        return new_punto.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg' : 'Error al crear punto'}),500
#----------------------------------------------------------------------------------------------------------------
#EDIT
def edit_punto(id_punto, nombre=None,latitud=None,longitud=None,direccion=None):
    try:
        punto = Punto.query.get(id_punto)
        if not punto:
            return {"error": "Punto no encontrado"}, 404
        if nombre is not None:
            punto.nombre = nombre
        if latitud is not None:
            punto.latitud = latitud
        if longitud is not None:
            punto.longitud = longitud
        if direccion is not None:
            punto.direccion = direccion
        db.session.commit()
        return punto.to_dict(), 200
    except Exception as e:
        print(f"ERROR: {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#DELETE
def delete_punto(id_punto):
    try:
        punto = Punto.query.get(id_punto)
        if not punto:
            return {"error": "Punto no encontrado"}, 404

        db.session.delete(punto)
        db.session.commit()
        return {"message": "Punto eliminado exitosamente"}, 200
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#GET ONE
def get_one_punto(id_punto):
    try:
        punto = Punto.query.get(id_punto) 
        if punto:
            return punto.to_dict(), 200 
        else:
            return {"error": "Punto no encontrado"}, 404  
    except Exception as error:
        print(f"ERROR {error}")
        return {"error": str(error)}, 500
#----------------------------------------------------------------------------------------------------------------
