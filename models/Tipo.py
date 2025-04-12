from config import db
class Tipo(db.Model):
    id_tipo = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    
    def __init__(self,tipo):
        self.tipo = tipo

    def to_dict(self):
        return {
            "id_tipo": self.id_tipo,
            "tipo": self.tipo
        }
