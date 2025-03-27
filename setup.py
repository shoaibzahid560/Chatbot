# setup.py
import os
import sys

# Define the base directory
base_dir = os.path.abspath(os.path.dirname(__file__))

# Define file structure and content
files = {
    os.path.join(base_dir, "app", "__init__.py"): """from flask import Flask
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
""",
    os.path.join(base_dir, "app", "main", "__init__.py"): """from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
""",
    os.path.join(base_dir, "app", "main", "routes.py"): """from flask import render_template
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')
""",
    os.path.join(base_dir, "app", "templates", "index.html"): """<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to the Construction Chatbot</h1>
    <p>This is the home page of your application.</p>
</body>
</html>
""",
    os.path.join(base_dir, "config.py"): """import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
""",
    os.path.join(base_dir, "run.py"): """from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
""",
    os.path.join(base_dir, ".env"): """SECRET_KEY=your-secret-key-here
"""
}

# Create directories if they don't exist
dirs = [
    os.path.join(base_dir, "app"),
    os.path.join(base_dir, "app", "main"),
    os.path.join(base_dir, "app", "templates")
]

for directory in dirs:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# Create files
for file_path, content in files.items():
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists (not modified): {file_path}")

print("\nAll files created successfully!")
print("Run your application with: python run.py")