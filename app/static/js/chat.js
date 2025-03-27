// Chat functionality
document.addEventListener('DOMContentLoaded', function() {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const messagesContainer = document.getElementById('messages-container');
    const userSelector = document.getElementById('user-selector');
    const projectSummary = document.getElementById('project-summary');
    
    let currentProjectId = null;

    // Initialize project buttons if available
    initializeProjectButtons();
    
    // Add event listener to user selector
    userSelector.addEventListener('change', function() {
        switchUser(this.value);
    });

    // Add event listener to message form
    messageForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const message = messageInput.value.trim();
        if (message) {
            addMessage('user', message);
            sendMessage(message);
            messageInput.value = '';
        }
    });

    function addMessage(sender, text) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `message-${sender}`);
        messageElement.textContent = text;
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function sendMessage(message) {
        fetch('/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                addMessage('bot', data.message);
                if (data.action === 'show_project_selector') {
                    showProjectSelector();
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('bot', 'Sorry, there was an error processing your message.');
        });
    }

    function showProjectSelector() {
        const projectSelector = document.getElementById('project-selector');
        if (projectSelector) {
            projectSelector.style.display = 'block';
            
            // Load project data for buttons
            loadProjectData();
        }
    }
    
    function switchUser(userId) {
        fetch('/api/switch_user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Reload the page to update the UI
                window.location.reload();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    function initializeProjectButtons() {
        const projectButtons = document.querySelectorAll('.project-btn');
        projectButtons.forEach(button => {
            button.addEventListener('click', function() {
                const projectId = this.getAttribute('data-project-id');
                selectProject(projectId);
            });
        });
        
        // Load project data for buttons if they exist
        if (projectButtons.length > 0) {
            loadProjectData();
        }
    }
    
    function loadProjectData() {
        fetch('/api/projects')
        .then(response => response.json())
        .then(projects => {
            const projectButtons = document.querySelectorAll('.project-btn');
            projectButtons.forEach(button => {
                const projectId = button.getAttribute('data-project-id');
                if (projects[projectId]) {
                    button.textContent = `${projects[projectId].name} (${projects[projectId].status})`;
                }
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    function selectProject(projectId) {
        fetch('/api/select_project', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ project_id: projectId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                currentProjectId = projectId;
                document.getElementById('project-selector').style.display = 'none';
                updateProjectSummary(data.project);
                addMessage('bot', `Project "${data.project.name}" selected. What would you like to know?`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    function updateProjectSummary(project) {
        const projectName = document.getElementById('project-name');
        const projectStatus = document.getElementById('project-status');
        const progressBar = document.getElementById('progress-bar');
        const completionPercentage = document.getElementById('completion-percentage');
        const projectTimeline = document.getElementById('project-timeline');
        
        projectName.textContent = project.name;
        projectStatus.textContent = project.status;
        projectStatus.className = `project-status status-${project.status.toLowerCase().replace(' ', '-')}`;
        progressBar.style.width = `${project.completion}%`;
        completionPercentage.textContent = `Completion: ${project.completion}%`;
        projectTimeline.textContent = project.timeline;
        
        projectSummary.style.display = 'block';
    }
});