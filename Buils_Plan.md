# BUILD_PLAN.md
## Splitwise-Inspired Shared Expenses Management System

## 1. Product Research

### Product Studied
The primary product researched was **Splitwise**.

### Research Approach
The following user workflows were analyzed:

1. Creating groups for shared expenses
2. Adding members to groups
3. Recording expenses
4. Splitting expenses among participants
5. Viewing balances
6. Settling debts
7. Tracking payment history

### Key Product Insights
Splitwise revolves around five core concepts:

- Users
- Groups
- Expenses
- Balances
- Settlements

The most important functionality is accurate expense allocation and balance calculation.

### Product Assumptions
To fit the assignment timeline, the following assumptions were made:

- A user can belong to multiple groups.
- Expenses belong to a group.
- An expense can have multiple participants.
- Split calculations are the core business logic.
- Relational databases are required.
- CSV import support can accelerate testing and data creation.

## 2. Architecture

### Tech Stack

**Backend**
- Python
- Django

**Database**
- SQLite

**Frontend**
- Django Templates
- HTML
- CSS

**Version Control**
- Git
- GitHub

### Database Schema

**User**
Stores application users.

**Group**
Stores expense groups.

**Group Membership**
Tracks which users belong to a group.

**Expense**
Stores expense information. Fields include:
- title
- amount
- currency
- expense_date
- paid_by
- split_type

**ExpenseParticipant**
Stores participant allocations. Supports:
- Equal splits
- Unequal splits
- Percentage splits
- Share-based splits

**ImportJob**
Tracks CSV imports.

**ImportAnomaly**
Tracks import validation issues.

### API / Application Structure

**Import Module**
Responsibilities:
- CSV upload
- CSV parsing
- Validation
- Expense creation
- Participant creation

**Expenses Module**
Responsibilities:
- Expense storage
- Participant management
- Split calculations

**Groups Module**
Responsibilities:
- Group ownership
- Membership tracking

### Frontend Structure

**Implemented pages:**
- CSV Upload Dashboard
- Import Report Dashboard

**Planned pages:**
- Login Page
- Group Dashboard
- Expense Creation Page
- Balance Dashboard
- Settlement Page

### Deployment Approach

**Target deployment:**
- Railway or Render

**Database:**
- SQLite for MVP

## 3. AI Collaboration Process

### AI Tool Used
ChatGPT

### Collaboration Method
The AI was used as a development collaborator for:

- Product analysis
- Data modeling
- CSV import workflow design
- Expense split logic
- Debugging
- Documentation

### Typical Workflow

1. Define a feature.
2. Discuss architecture.
3. Generate implementation approach.
4. Review generated code.
5. Modify manually.
6. Test locally.
7. Commit changes.
8. Update documentation.

### Validation Process
AI-generated outputs were not accepted blindly. Each change was:

- Reviewed manually
- Tested locally
- Adjusted where necessary

## 4. Tradeoffs

### Simplifications
To fit the assignment timeline:

- CSV import workflow was prioritized.
- SQLite was used instead of PostgreSQL.
- Initial frontend uses Django templates.

### Deferred Features
The following features are planned but not fully implemented:

- Authentication
- Group management UI
- Settlements UI
- Real-time expense chat

### Future Improvements
With more time, the following would be added:

- Django authentication
- Settlement workflow
- Balance dashboard
- Real-time chat using WebSockets
- Notifications
- Production-grade deployment
