# AI_CONTEXT.md

## Assignment Goal

Build a simplified Splitwise-inspired application using AI as the primary development collaborator.

The goal is not to perfectly clone Splitwise but to understand:

- Product behavior
- Expense sharing workflows
- Balance calculations
- Engineering tradeoffs
- AI-assisted development

---

## Product Understanding

Splitwise is a shared-expense management platform.

Users create groups, record expenses, split costs, track balances, and settle debts.

Core entities identified:

- Users
- Groups
- Expenses
- Participants
- Balances
- Settlements

---

## MVP Scope

### Implemented

**Expense Management**
- Expense model
- Expense participant model

**Split Types**
- Equal
- Unequal
- Percentage
- Share

**CSV Import System**
- Upload CSV
- Parse rows
- Validate records
- Create expenses
- Create participants

**Anomaly Detection**

Implemented anomaly types:
- Missing payer
- Missing currency
- Unknown payer
- Unknown participant
- Settlement detection
- Duplicate expenses
- Membership violations
- Negative amounts
- Invalid percentage allocations

**Reporting**
- Import dashboard
- Import report dashboard

### Planned

**Authentication**
- Login
- Logout

**Groups**
- Create group
- Add members
- Remove members

**Balances**
- Group balance summary
- Individual balance summary

**Settlements**
- Record payments
- Settle debts

**Communication**
- Expense comments
- Real-time updates

---

## Technical Architecture

### Backend

**Framework:** Django

**Reason:**
- Rapid development
- Built-in ORM
- Admin support
- Authentication support

### Database

**Choice:** SQLite

**Reason:**
- Relational
- Lightweight
- Suitable for assignment scope

---

## Application Modules

**Accounts**
Purpose: User management.

**Groups**
Purpose: Group creation and membership management.

**Expenses**
Purpose: Expense storage and participant allocations.

**Imports**
Purpose: CSV processing and anomaly detection.

**Settlements**
Purpose: Future settlement workflow.

---

## Database Design

### Expense

Fields:
- title
- amount
- currency
- expense_date
- paid_by
- split_type

Relationships:
- belongs to group
- belongs to payer
- has participants

### ExpenseParticipant

Fields:
- expense
- user
- share_amount
- percentage

Purpose: Stores final calculated allocations.

### ImportJob

Purpose: Tracks import execution.

Fields:
- file_name
- status

### ImportAnomaly

Purpose: Tracks validation issues.

Fields:
- row_number
- issue_type
- action_taken

---

## CSV Import Workflow

1. User uploads CSV.
2. CSV is parsed.
3. Each row is validated.
4. Anomalies are detected.
5. Expense is created.
6. Participants are generated.
7. Import report is produced.

---

## Split Logic

**Equal Split**
Amount divided equally among participants.

**Unequal Split**
Explicit amounts supplied for each participant.

**Percentage Split**
Percentages supplied for participants.
Validation: total percentage should equal 100.

**Share Split**
Relative share values supplied. Allocation is calculated proportionally.

---

## Frontend Structure

### Upload Page

Purpose: Upload expense CSV files.

Features:
- File upload
- Dashboard layout

### Report Page

Purpose: Display import results.

Displays:
- Job status
- Expense counts
- Anomaly counts
- Anomaly details

---

## Testing Strategy

### Manual Testing

Primary dataset: `Expenses Export.csv`

**Validated:**
- Expense creation
- Participant creation
- Split calculations
- Anomaly generation
- CSV processing

---

## AI Collaboration Log

### AI Responsibilities

Used for:
- Product analysis
- Data model review
- CSV import architecture
- Split calculation design
- Debugging assistance
- UI suggestions
- Documentation generation

### Human Responsibilities

- Feature decisions
- Code review
- Testing
- Bug fixing
- Final implementation choices

---

## Major Changes During Development

**Initial Version**
Basic import workflow.

**Iteration 1**
Added anomaly detection.

**Iteration 2**
Added settlement detection.

**Iteration 3**
Added membership validation.

**Iteration 4**
Added percentage and share allocations.

**Iteration 5**
Added dashboard-based frontend.

---

## Known Limitations

- Authentication not yet completed.
- Settlement workflow not yet completed.
- Group management UI not yet completed.
- Real-time chat not yet completed.
- SQLite used for development.

---

## Future Enhancements

- Django authentication
- Group management
- Balance dashboard
- Settlement engine
- Real-time communication
- PostgreSQL deployment
- Production hosting

---

## Reproducibility Notes

A developer or AI agent should be able to recreate this project by:

1. Creating the Django project structure.
2. Implementing the described models.
3. Implementing split calculation logic.
4. Implementing the CSV import workflow.
5. Implementing anomaly detection.
6. Creating the upload and reporting dashboards.
7. Following the architecture and workflows described in this document.
