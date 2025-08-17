# Welcome Flow

## Project Description
**Welcome Flow** is a system for sending welcome emails and reminders to new users built with **Django**, **Django REST Framework**, **Celery**, and **Redis**.  
The project automatically sends welcome emails, profile completion reminders.


## Features
- User registration and data storage in the database
- Sending HTML-based welcome emails
- Scheduled reminders for profile completion or other messages
- Celery integration for managing background and scheduled tasks
- Tracking and managing email sending status


## Installation & Setup

### Requirements
- Python >= 3.10
- Django >= 4.2
- Redis (for Celery)
- PostgreSQL or SQLite

### Steps
1. Clone the repository:
```bash
git clone <repository_url>
cd welcome-flow
```

### Install dependencies
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### Set up .env file
```bash
DJANGO_SECRET_KEY=your_secret_key
DEBUG=1
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

### Running Celery
```bash
celery -A config worker -l info
```

### API Endpoints

## User Registration
- URL: /api/register/
Method: POST
Body:
```bash
{
    "username": "username",
    "email": "email@example.com",
    "password": "securepassword"
}
```