# SCOPE.md

Defines what is in scope for this project, what has been implemented, what remains pending against the assignment's minimum requirements, and what is explicitly out of scope.

---

## Assignment Minimum Requirements (for reference)

Per the assignment brief, the minimum product requirements are:

1. Login module
2. Create and manage groups (invite, add, remove users)
3. Create and manage expenses
   - Split equally, unequally, by percentage, and by share
   - User chat in an expense (real-time updates)
   - Group-wise balances and individual balance summary
   - Settle debts or record payments
4. Relational database only

---

## Implemented (In Scope, Done)

### Expense Management
- Expense model with title, amount, currency, date, payer, split type
- ExpenseParticipant model storing per-participant allocations

### Split Types
- Equal
- Unequal
- Percentage (validated to sum to 100)
- Share-based (proportional allocation)

### CSV Import Pipeline
- CSV upload
- Row-by-row parsing and validation
- Expense and participant creation from valid rows
- Import report generation (job status, expense counts, anomaly counts)

### Anomaly Detection
- Missing payer / missing currency
- Unknown payer / unknown participant
- Settlement detection
- Duplicate expenses
- Membership violations
- Negative amounts
- Invalid percentage allocations

### Frontend
- CSV Upload Dashboard
- Import Report Dashboard

### Database
- SQLite (relational, satisfies the relational-DB requirement)

---

## In Scope but Not Yet Implemented (Gap vs. Minimum Requirements)

These items are part of the assignment's minimum requirements but are currently **not built**:

| Requirement | Status |
|---|---|
| Login module | Not started |
| Group creation / management (invite, add, remove members) | Not started |
| Group-wise balance summary | Not started |
| Individual balance summary | Not started |
| Settle debts / record payments | Not started |
| Real-time chat within an expense | Not started |

These are the priority items for closing the gap against the stated assignment scope, in roughly the order listed (auth → groups → balances/settlements → chat, since each later item depends on the ones before it).

---

## Out of Scope (Not Planned for This Assignment)

- Production-grade deployment (PostgreSQL, containerization, CI/CD)
- Notifications (email/push)
- Multi-currency conversion / exchange rate handling
- Mobile app or native client
- Multi-tenant / organization-level access controls
- Audit logs beyond import anomaly tracking

---

## Assumptions Underlying Current Scope

- A user can belong to multiple groups.
- Every expense belongs to exactly one group.
- An expense can have multiple participants, each with one allocation record.
- Split calculation correctness is treated as the core business logic of the product — prioritized ahead of UI completeness for auth/groups/settlements.
- CSV import is treated as a legitimate first-class workflow (not just a dev/testing convenience), since it accelerates generating realistic multi-expense, multi-participant datasets for testing balance and split logic.
- SQLite is acceptable for the assignment's scope; PostgreSQL migration is deferred to a "production" phase that is itself out of scope for this submission.

---

## Why This Matters for Evaluation

The assignment evaluators will compare submitted code against the minimum requirements list and may attempt to recreate the app from AI_CONTEXT.md. The "In Scope but Not Yet Implemented" table above is the most direct map of remaining work needed before the submission satisfies the stated minimum product requirements — everything in that table should move to the "Implemented" section before final submission, or be explicitly justified as a tradeoff in BUILD_PLAN.md if time does not allow.
