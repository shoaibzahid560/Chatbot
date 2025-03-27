# File: app/__init__.py
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


# File: app/main/__init__.py
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes


# File: app/main/routes.py
from flask import render_template
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')


# File: config.py
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


# File: run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)