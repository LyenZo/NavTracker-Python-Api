from config import db
class Rastreo(db.Model):
    id_rastreo = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float(precision=6), nullable=False)
    lng = db.Column(db.Float(precision=6), nullable=False)
    altitud = db.Column(db.Numeric(10, 3), nullable=False)
    velocidad = db.Column(db.Numeric(5, 3), nullable=False)
    hora = db.Column(db.Time, nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def __init__(self, lat,lng,altitud,velocidad,hora,fecha):
        self.lat = lat
        self.lng = lng
        self.altitud = altitud
        self.velocidad = velocidad
        self.hora = hora
        self.fecha = fecha


    def to_dict(self):
        return {
            "id_rastreo": self.id_rastreo,
            "lat": self.lat,
            "lng": self.lng,
            "altitud": float(self.altitud),
            "velocidad": float(self.velocidad),
            "hora": self.hora.strftime("%H:%M:%S"),
            "fecha": self.fecha.strftime("%Y-%m-%d")
        }