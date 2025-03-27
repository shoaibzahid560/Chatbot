# app/main/routes.py
from flask import render_template
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Construction Project Management')

@bp.route('/simple')
def simple():
    return render_template('simple_index.html', title='Simple Construction Chat')