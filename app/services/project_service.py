from data.projects import project_data

def get_all_projects():
    """Get all projects"""
    return project_data

def get_project_by_id(project_id):
    """Get project by ID"""
    return project_data.get(project_id)

def get_project_milestones(project_id):
    """Get project milestones"""
    project = get_project_by_id(project_id)
    return project['milestones'] if project else []

def get_project_issues(project_id):
    """Get project issues"""
    project = get_project_by_id(project_id)
    return project['issues'] if project else []

def get_project_budget(project_id):
    """Get project budget"""
    project = get_project_by_id(project_id)
    return project['budget'] if project else None

def calculate_budget_metrics(project_id):
    """Calculate budget metrics"""
    budget = get_project_budget(project_id)
    if not budget:
        return None
    
    return {
        'percentage_spent': (budget['spent'] / budget['allocated']) * 100,
        'percentage_remaining': (budget['remaining'] / budget['allocated']) * 100,
        'is_over_budget': budget['spent'] > budget['allocated']
    }