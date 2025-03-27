# app.py
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def index():
    return render_template('index.html', title='Construction Project Management')

@app.route('/simple')
def simple():
    """Route for testing the simplified version"""
    return render_template('simple_index.html', title='Simple Construction Chat')

if __name__ == '__main__':
    app.run(debug=True)