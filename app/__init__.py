from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, jwt
from .routes.auth_routes import auth_bp
from .routes.product_routes import product_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configura CORS permitiendo todos los orígenes y el encabezado Authorization
    CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}}, headers=['Content-Type', 'Authorization'])

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    return app
