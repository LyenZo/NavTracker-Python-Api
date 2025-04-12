from flask import Flask
from dotenv import load_dotenv
import os

from flask_cors import CORS 
from flask_jwt_extended import JWTManager

from config import db, migrate

# Carga variables de entorno desde el archivo .env
load_dotenv()

# Inicialización de la app Flask
app = Flask(__name__)

# Permitir CORS
CORS(app, resources={r"/api/*": {"origins": ["https://editor.swagger.io"]}})

# Configuración del JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'qwertyuiop')  # Usa variable de entorno como fallback
jwt = JWTManager(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos y migraciones
db.init_app(app)
migrate.init_app(app, db)

# Importación de modelos (para que los reconozca Flask-Migrate)
from models.Punto import Punto
from models.Rastreo import Rastreo
from models.Ruta import Ruta
from models.Tipo import Tipo
from models.Usuario import Usuario
from models.Vehiculo import Vehiculo

# Importación y registro de blueprints
from routes.punto import punto_bp
from routes.rastreo import rastreo_bp
from routes.ruta import ruta_bp
from routes.tipo import tipo_bp
from routes.usuario import usuario_bp
from routes.vehiculo import vehiculo_bp

app.register_blueprint(punto_bp, url_prefix='/api/punto_ruta')
app.register_blueprint(rastreo_bp, url_prefix='/api/rastreo')
app.register_blueprint(ruta_bp, url_prefix='/api/ruta')
app.register_blueprint(tipo_bp, url_prefix='/api/u_tipo')  # Arreglado prefijo
app.register_blueprint(usuario_bp, url_prefix='/api/usuario')
app.register_blueprint(vehiculo_bp, url_prefix='/api/vehiculo')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
