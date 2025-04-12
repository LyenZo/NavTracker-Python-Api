from config import db
class Ruta(db.Model):
    id_ruta = db.Column(db.Integer, primary_key=True)
    id_conductor = db.Column(db.Integer, nullable=False)
    id_pasajero = db.Column(db.Integer, nullable=False)
    lat_inicio = db.Column(db.Numeric(9, 6), nullable=False)
    lon_inicio = db.Column(db.Numeric(9, 6), nullable=False)
    lat_final = db.Column(db.Numeric(9, 6), nullable=False)
    lon_final = db.Column(db.Numeric(9, 6), nullable=False)
    f_inicio = db.Column(db.DateTime, nullable=False)
    f_final = db.Column(db.DateTime, nullable=False)
    distancia = db.Column(db.Numeric(9, 6), nullable=False)
    
    def __init__(self,id_conductor,id_pasajero,lat_inicio,lat_final,lon_inicio,lon_final,f_inicio,f_final,distancia):
        self.id_conductor = id_conductor
        self.id_pasajero = id_pasajero
        self.lat_inicio = lat_inicio
        self.lat_final = lat_final
        self.lon_inicio = lon_final
        self.lon_final = lon_final
        self.f_inicio = f_inicio
        self.f_final = f_final
        self.distancia = distancia
        
        

    def to_dict(self):
        return {
            "id_ruta": self.id_ruta,
            "id_conductor": self.id_conductor,
            "id_pasajero": self.id_pasajero,
            "lat_inicio": float(self.lat_inicio),
            "lon_inicio": float(self.lon_inicio),
            "lat_final": float(self.lat_final),
            "lon_final": float(self.lon_final),
            "f_inicio": self.f_inicio.strftime("%Y-%m-%d %H:%M:%S"),
            "f_final": self.f_final.strftime("%Y-%m-%d %H:%M:%S"),
            "distancia": float(self.distancia)
        }