# Mock project data
project_data = {
    "P001": {
        "name": "Riverside Apartments",
        "status": "In Progress",
        "completion": 65,
        "timeline": "March 2025 - October 2025",
        "budget": {
            "allocated": 3500000,
            "spent": 2275000,
            "remaining": 1225000
        },
        "issues": [
            {"id": "I001", "description": "Delayed material delivery", "status": "Resolved", "date": "2025-02-15"},
            {"id": "I002", "description": "Permit approval pending", "status": "Open", "date": "2025-03-10"}
        ],
        "resources": {
            "workers": 42,
            "equipment": ["Excavator", "Crane", "Concrete Mixer"]
        },
        "milestones": [
            {"name": "Foundation", "status": "Completed", "date": "2025-04-15"},
            {"name": "Structural Framework", "status": "In Progress", "date": "2025-06-30"},
            {"name": "Plumbing & Electrical", "status": "Not Started", "date": "2025-08-15"},
            {"name": "Interior Finishing", "status": "Not Started", "date": "2025-09-30"}
        ]
    },
    "P002": {
        "name": "Downtown Office Complex",
        "status": "Planning",
        "completion": 10,
        "timeline": "May 2025 - December 2025",
        "budget": {
            "allocated": 5800000,
            "spent": 580000,
            "remaining": 5220000
        },
        "issues": [
            {"id": "I003", "description": "Zoning approval delay", "status": "Open", "date": "2025-03-05"}
        ],
        "resources": {
            "workers": 15,
            "equipment": ["Surveying Equipment"]
        },
        "milestones": [
            {"name": "Site Preparation", "status": "In Progress", "date": "2025-05-20"},
            {"name": "Foundation", "status": "Not Started", "date": "2025-06-15"},
            {"name": "Structural Framework", "status": "Not Started", "date": "2025-08-30"},
            {"name": "Completion", "status": "Not Started", "date": "2025-12-15"}
        ]
    },
    "P003": {
        "name": "Community Center Renovation",
        "status": "Completed",
        "completion": 100,
        "timeline": "September 2024 - February 2025",
        "budget": {
            "allocated": 1200000,
            "spent": 1150000,
            "remaining": 50000
        },
        "issues": [],
        "resources": {
            "workers": 0,
            "equipment": []
        },
        "milestones": [
            {"name": "Demolition", "status": "Completed", "date": "2024-10-01"},
            {"name": "Structural Modifications", "status": "Completed", "date": "2024-11-15"},
            {"name": "Electrical & Plumbing", "status": "Completed", "date": "2024-12-20"},
            {"name": "Interior Finishing", "status": "Completed", "date": "2025-01-25"},
            {"name": "Final Inspection", "status": "Completed", "date": "2025-02-10"}
        ]
    }
}