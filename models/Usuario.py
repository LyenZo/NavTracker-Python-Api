from config import db
from werkzeug.security import generate_password_hash, check_password_hash
class Usuario(db.Model):
    id_u = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    ap_pat = db.Column(db.String(20), nullable=False)
    ap_mat = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    n_tel = db.Column(db.String(20), nullable=True)
    id_tipo = db.Column(db.Integer, nullable=False)
    id_vehiculo = db.Column(db.Integer, nullable=True)
    
    def __init__(self,nombre,ap_pat,ap_mat,email,password,n_tel,id_tipo,id_vehiculo):
        self.nombre = nombre
        self.ap_pat = ap_pat
        self.ap_mat = ap_mat
        self.email = email
        self.password = generate_password_hash(password)
        self.n_tel = n_tel
        self.id_tipo = id_tipo
        self.id_vehiculo = id_vehiculo
        
    def check_password(self,password):
        return check_password_hash(self.password,password)
    
    def to_dict(self):
        return {
            "id_u": self.id_u,
            "nombre": self.nombre,
            "ap_pat": self.ap_pat,
            "ap_mat": self.ap_mat,
            "email": self.email,
            "n_tel": self.n_tel,
            "id_tipo": self.id_tipo,
            "id_vehiculo": self.id_vehiculo
        }