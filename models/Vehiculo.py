from config import db

class Vehiculo(db.Model):
    id_vehiculo = db.Column(db.Integer, primary_key=True)
    vehiculo = db.Column(db.String(20), nullable=False)

    def __init__(self, vehiculo):
        self.vehiculo = vehiculo

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "vehiculo": self.vehiculo
        }
