from app.services.project_service import get_project_by_id

def process_message(message, active_project_id):
    """Process incoming messages and determine appropriate response"""
    lower_msg = message.lower()
    
    # Check for project selection
    if 'project' in lower_msg and ('select' in lower_msg or 'choose' in lower_msg):
        return 'SHOW_PROJECT_SELECTOR'
    
    # If no project is selected, prompt to select one
    if not active_project_id:
        return "Please select a project first by typing 'select project'."
    
    project = get_project_by_id(active_project_id)
    
    # Check for project status
    if 'status' in lower_msg:
        return f"Project \"{project['name']}\" is currently {project['status']} with {project['completion']}% completion. The timeline is {project['timeline']}."
    
    # Check for budget inquiries
    if any(word in lower_msg for word in ['budget', 'cost', 'money']):
        budget = project['budget']
        return f"Budget for {project['name']}: Allocated: ${budget['allocated']:,}, Spent: ${budget['spent']:,}, Remaining: ${budget['remaining']:,}"
    
    # Check for issue reports
    if any(word in lower_msg for word in ['issue', 'problem']):
        issues = project['issues']
        if not issues:
            return f"No issues reported for project {project['name']}."
        else:
            return f"Issues for {project['name']}:\n" + "\n".join([
                f"- {issue['description']} ({issue['status']}) - Reported on {issue['date']}"
                for issue in issues
            ])
    
    # Check for milestone inquiries
    if any(word in lower_msg for word in ['milestone', 'progress']):
        milestones = project['milestones']
        return f"Milestones for {project['name']}:\n" + "\n".join([
            f"- {milestone['name']}: {milestone['status']} (Target: {milestone['date']})"
            for milestone in milestones
        ])
    
    # Check for resource inquiries
    if any(word in lower_msg for word in ['resource', 'worker', 'equipment']):
        resources = project['resources']
        equipment_str = ', '.join(resources['equipment']) if resources['equipment'] else 'None'
        return f"Resources for {project['name']}:\n- Workers: {resources['workers']}\n- Equipment: {equipment_str}"
    
    # Help message
    if 'help' in lower_msg:
        return "You can ask about:\n- Project Status\n- Budget Information\n- Current Issues\n- Milestones\n- Resources\n\nFirst, select a project by typing 'select project'."
    
    # Default response
    return "I'm not sure how to answer that. Try asking about project status, budget, issues, milestones, or resources."