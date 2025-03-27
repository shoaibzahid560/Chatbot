from flask import Blueprint, render_template, request, jsonify, session
from app.services.chat_service import process_message
from app.services.auth_service import get_user_by_id, get_all_users
from app.services.project_service import get_all_projects, get_project_by_id
from data.projects import project_data
from data.users import user_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat')
def chat():
    users = get_all_users()
    # Default to first user if none selected
    current_user_id = session.get('user_id', list(users.keys())[0])
    current_user = get_user_by_id(current_user_id)
    
    return render_template(
        'chat.html', 
        users=users, 
        current_user=current_user,
        current_user_id=current_user_id
    )

@main.route('/api/switch_user', methods=['POST'])
def switch_user():
    data = request.get_json()
    user_id = data.get('user_id')
    
    if user_id in user_data:
        session['user_id'] = user_id
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid user ID'})

@main.route('/api/projects')
def get_projects():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify([])
    
    user = get_user_by_id(user_id)
    accessible_projects = {}
    
    for project_id in user['project_access']:
        if project_id in project_data:
            accessible_projects[project_id] = project_data[project_id]
    
    return jsonify(accessible_projects)

@main.route('/api/select_project', methods=['POST'])
def select_project():
    data = request.get_json()
    project_id = data.get('project_id')
    
    user_id = session.get('user_id')
    user = get_user_by_id(user_id)
    
    if not user or project_id not in user['project_access']:
        return jsonify({'status': 'error', 'message': 'Access denied'})
    
    session['project_id'] = project_id
    return jsonify({'status': 'success', 'project': get_project_by_id(project_id)})

@main.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message_text = data.get('message')
    
    project_id = session.get('project_id')
    
    response = process_message(message_text, project_id)
    
    if response == 'SHOW_PROJECT_SELECTOR':
        return jsonify({
            'status': 'success',
            'message': 'Please select a project from the list below.',
            'action': 'show_project_selector'
        })
    
    return jsonify({
        'status': 'success',
        'message': response
    })