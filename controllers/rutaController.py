from models.Ruta import Ruta
from flask import jsonify
from config import db

#----------------------------------------------------------------------------------------------------------------
#GET ALL
def get_all_rutas():
    try:
        return[ruta.to_dict() for ruta in Ruta.query.all()]
    except Exception as error:
        print(f"ERROR {error}")
#----------------------------------------------------------------------------------------------------------------
#CREATE
def create_ruta(id_conductor,id_pasajero,lat_inicio,lon_inicio,lat_final,lon_final,f_inicio,f_final,distancia):
    try:
        new_ruta = Ruta(id_conductor,id_pasajero,lat_inicio,lon_inicio,lat_final,lon_final,f_inicio,f_final,distancia)
        db.session.add(new_ruta)
        db.session.commit()
        return new_ruta.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg' : 'Error al crear ruta'}),500
#----------------------------------------------------------------------------------------------------------------
#EDIT
def edit_ruta(id_ruta, id_conductor=None,id_pasajero=None,lat_inicio=None,lon_inicio=None,lat_final=None,lon_final=None,f_inicio=None,f_final=None,distancia=None):
    try:
        ruta = Ruta.query.get(id_ruta)
        if not ruta:
            return {"error": "Ruta no encontrada"}, 404
        if id_conductor is not None:
            ruta.id_conductor = id_conductor
        if id_pasajero is not None:
            ruta.id_pasajero = id_pasajero
        if id_conductor is not None:
            ruta.id_conductor = id_conductor
        if lat_inicio is not None:
            ruta.lat_inicio = lat_inicio
        if lat_final is not None:
            ruta.lat_final = lat_final
        if lon_inicio is not None:
            ruta.lon_inicio = lon_inicio
        if lon_final is not None:
            ruta.lon_final = lon_final
        if f_inicio is not None:
            ruta.f_inicio = f_inicio
        if f_final is not None:
            ruta.f_final = f_final
        if distancia is not None:
            ruta.distancia = distancia
        db.session.commit()
        return ruta.to_dict(), 200
    except Exception as e:
        print(f"ERROR: {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#DELETE
def delete_ruta(id_ruta):
    try:
        ruta = Ruta.query.get(id_ruta)
        if not ruta:
            return {"error": "Ruta no encontrado"}, 404

        db.session.delete(ruta)
        db.session.commit()
        return {"message": "Ruta eliminada exitosamente"}, 200
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#GET ONE
def get_one_ruta(id_ruta):
    try:
        ruta = Ruta.query.get(id_ruta) 
        if ruta:
            return ruta.to_dict(), 200 
        else:
            return {"error": "ruta no encontrado"}, 404  
    except Exception as error:
        print(f"ERROR {error}")
        return {"error": str(error)}, 500
#----------------------------------------------------------------------------------------------------------------

