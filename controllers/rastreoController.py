from models.Rastreo import Rastreo
from flask import jsonify
from config import db

#----------------------------------------------------------------------------------------------------------------
#GET ALL
def get_all_rastreos():
    try:
        return[rastreo.to_dict() for rastreo in Rastreo.query.all()]
    except Exception as error:
        print(f"ERROR {error}")
#----------------------------------------------------------------------------------------------------------------
#CREATE
def create_rastreo(lat,lng,altitud,velocidad,hora,fecha):
    try:
        new_rastreo = Rastreo(lat,lng,altitud,velocidad,hora,fecha)
        db.session.add(new_rastreo)
        db.session.commit()
        return new_rastreo.to_dict()
    except Exception as e:
        print(f"ERROR {e}")
        return jsonify({'msg' : 'Error al crear rastreo'}),500
#----------------------------------------------------------------------------------------------------------------
#EDIT
def edit_rastreo(id_rastreo, lat=None,lng=None,altitud=None,velocidad=None,hora=None,fecha=None):
    try:
        rastreo = Rastreo.query.get(id_rastreo)
        if not rastreo:
            return {"error": "Rastreo no encontrado"}, 404
        if lat is not None:
            rastreo.lat = lat
        if lng is not None:
            rastreo.lng = lng
        if altitud is not None:
            rastreo.altitud = altitud
        if velocidad is not None:
            rastreo.velocidad = velocidad
        if hora is not None:
            rastreo.hora = hora
        if fecha is not None:
            rastreo.fecha = fecha
        db.session.commit()
        return rastreo.to_dict(), 200
    except Exception as e:
        print(f"ERROR: {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#DELETE
def delete_rastreo(id_rastreo):
    try:
        rastreo = Rastreo.query.get(id_rastreo)
        if not rastreo:
            return {"error": "Rastreo no encontrado"}, 404

        db.session.delete(rastreo)
        db.session.commit()
        return {"message": "Rastreo eliminado exitosamente"}, 200
    except Exception as e:
        print(f"ERROR {e}")
        return {"error": str(e)}, 500
#----------------------------------------------------------------------------------------------------------------
#GET ONE
def get_one_rastreo(id_rastreo):
    try:
        rastreo = Rastreo.query.get(id_rastreo) 
        if rastreo:
            return rastreo.to_dict(), 200 
        else:
            return {"error": "Rastreo no encontrado"}, 404  
    except Exception as error:
        print(f"ERROR {error}")
        return {"error": str(error)}, 500
#----------------------------------------------------------------------------------------------------------------
