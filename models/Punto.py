from config import db
class Punto(db.Model):
    id_punto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    latitud = db.Column(db.Numeric(18, 15), nullable=False)
    longitud = db.Column(db.Numeric(18, 15), nullable=False)
    direccion = db.Column(db.String(20), nullable=True)
    
    def __init__(self,nombre,latitud,longitud,direccion):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion
    
    def to_dict(self):
        return {
            "id_punto": self.id_punto,
            "nombre": self.nombre,
            "latitud": float(self.latitud),
            "longitud": float(self.longitud),
            "direccion": self.direccion
        }
