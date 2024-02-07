from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from .extensions import mongo
import os

def create_app():
    app = Flask(__name__)
    # initialize Mongo
    app.config['MONGO_URI'] = os.getenv("MONGO_URL")
    mongo.init_app(app)

    # middleware and configuration setup
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)
    env_config = os.getenv("FLASK_ENV", default="DevelopmentConfig")
    app.config.from_object(f"app.config.{env_config}")
                        
    # setup CORS and register blueprints/routes
    CORS(app, resources={r"/*": {"origins": "*"}})
    from .main import main as main_bp
    app.register_blueprint(main_bp)
    
    return app
