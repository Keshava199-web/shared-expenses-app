# Shared Expenses Management System

A Splitwise-inspired expense sharing application built with Django and SQLite. The system supports multiple expense-splitting methods, balance tracking, and bulk expense imports via CSV with built-in anomaly detection.

This project was developed as part of an internship assignment focused on product analysis, AI-assisted development, software engineering practices, and documentation.

## Features

### Expense Management
- Expense creation
- Expense participants
- Multiple split methods per expense

### Split Types
- Equal split
- Unequal split
- Percentage-based split
- Share-based split

### CSV Import
- Bulk CSV upload
- Automatic expense creation from CSV data
- Automatic participant creation from CSV data

### Anomaly Detection
The CSV import pipeline flags the following issues during processing:
- Missing payer
- Missing currency
- Unknown payer
- Unknown participant
- Settlement detection
- Duplicate expenses
- Membership violations
- Negative amounts
- Invalid percentage allocations

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS |
| Version Control | Git, GitHub |

## Setup

```bash
git clone <repository-url>
cd shared-expenses-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## AI Usage

**Primary AI collaborator:** ChatGPT

AI assistance was used for:
- Architecture discussions
- Model design reviews
- CSV import workflow design
- Split calculation logic
- Debugging
- Documentation

All AI-generated code was manually reviewed, tested, and modified where required.

## Future Improvements

- Authentication
- Settlement workflow
- Group management UI
- Real-time expense chat
- Notifications
- Production deployment
