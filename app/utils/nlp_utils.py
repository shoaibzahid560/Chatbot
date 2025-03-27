# Simple NLP functions for the chatbot

# List of keywords for different query types
STATUS_KEYWORDS = ['status', 'progress', 'completion', 'done', 'finished']
BUDGET_KEYWORDS = ['budget', 'cost', 'money', 'spend', 'spending', 'expense', 'financial']
ISSUE_KEYWORDS = ['issue', 'problem', 'trouble', 'challenge', 'difficulty', 'error', 'mistake']
MILESTONE_KEYWORDS = ['milestone', 'phase', 'stage', 'step', 'timeline', 'schedule']
RESOURCE_KEYWORDS = ['resource', 'worker', 'staff', 'people', 'team', 'equipment', 'tool', 'machine']

def detect_intent(message):
    """Detect the intent of the user message"""
    message = message.lower()
    
    # Check for project selection intent
    if ('select' in message or 'choose' in message or 'pick' in message) and 'project' in message:
        return 'select_project'
    
    # Check for status intent
    if any(keyword in message for keyword in STATUS_KEYWORDS):
        return 'status'
    
    # Check for budget intent
    if any(keyword in message for keyword in BUDGET_KEYWORDS):
        return 'budget'
    
    # Check for issue intent
    if any(keyword in message for keyword in ISSUE_KEYWORDS):
        return 'issue'
    
    # Check for milestone intent
    if any(keyword in message for keyword in MILESTONE_KEYWORDS):
        return 'milestone'
    
    # Check for resource intent
    if any(keyword in message for keyword in RESOURCE_KEYWORDS):
        return 'resource'
    
    # Check for help intent
    if 'help' in message or 'guide' in message or 'assist' in message:
        return 'help'
    
    # Default to unknown intent
    return 'unknown'

def extract_project_reference(message, project_data):
    """Try to extract a project reference from the message"""
    message = message.lower()
    
    for project_id, project in project_data.items():
        if project['name'].lower() in message:
            return project_id
    
    return None

def clean_message(message):
    """Remove unnecessary words and characters from message"""
    message = message.lower()
    # Remove punctuation
    message = ''.join(c for c in message if c.isalnum() or c.isspace())
    
    # List of stop words to remove
    stop_words = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'am', 'can', 'could', 'would', 'should']
    
    # Split message into words and filter out stop words
    words = message.split()
    filtered_words = [word for word in words if word not in stop_words]
    
    return ' '.join(filtered_words)