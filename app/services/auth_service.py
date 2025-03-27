from data.users import user_data

def get_user_by_id(user_id):
    """Get user by ID"""
    return user_data.get(user_id)

def get_all_users():
    """Get all users"""
    return user_data

def user_has_project_access(user_id, project_id):
    """Check if user has access to project"""
    user = get_user_by_id(user_id)
    return user and project_id in user['project_access']

def get_user_projects(user_id):
    """Get projects accessible to user"""
    user = get_user_by_id(user_id)
    return user['project_access'] if user else []