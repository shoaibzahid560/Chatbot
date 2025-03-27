from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    csrf = CSRFProtect()
    csrf.init_app(app)
    
    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
