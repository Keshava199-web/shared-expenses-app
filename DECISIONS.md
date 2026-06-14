# DECISIONS.md

A log of key implementation decisions made during the project, with context and rationale. This complements AI_CONTEXT.md and BUILD_PLAN.md by isolating *why* choices were made, separate from *what* was built.

---

## 1. Backend Framework: Django

**Decision:** Use Django as the backend framework.

**Rationale:**
- Built-in ORM simplifies relational schema work (Expense, ExpenseParticipant, Group, etc.)
- Built-in admin panel useful for inspecting imported data during development
- Built-in authentication framework available for future login work
- Fast to scaffold within a short assignment timeline

**Status:** Implemented.

---

## 2. Database: SQLite

**Decision:** Use SQLite instead of PostgreSQL for the MVP.

**Rationale:**
- Relational database requirement satisfied (per assignment constraints)
- Zero setup/configuration overhead — works out of the box with Django
- Sufficient for assignment-scale data volumes

**Tradeoff:** Not production-grade; would need migration to PostgreSQL for real deployment (concurrent writes, hosting compatibility with Railway/Render).

**Status:** Implemented for development. Migration to PostgreSQL listed as a future enhancement.

---

## 3. Frontend: Django Templates (not SPA)

**Decision:** Use server-rendered Django templates rather than a separate frontend framework (React, Vue, etc.).

**Rationale:**
- Avoids splitting effort across a separate frontend build/deploy pipeline
- CSV upload and report dashboards are form/table-heavy — well suited to templates
- Keeps the stack to a single deployable unit

**Tradeoff:** Real-time features (expense chat) are harder to bolt on later without introducing JS-side state management or WebSockets.

**Status:** Implemented for upload/report pages. Revisit if real-time chat is built.

---

## 4. CSV Import Prioritized Over Manual UI Workflows

**Decision:** Build the CSV import + anomaly detection pipeline before building manual group/expense creation UI.

**Rationale:**
- CSV import accelerates test data generation, which unblocks testing of split logic and balance calculations
- Anomaly detection demonstrates data validation thinking, which is a meaningful engineering signal
- Manual CRUD UI for groups/expenses is comparatively lower-risk and faster to add once models are stable

**Tradeoff:** Core assignment-required features (login, group management, settlements) were pushed later in the schedule and remain incomplete.

**Status:** Implemented. Direct consequence is the current gap against assignment minimum requirements (see SCOPE.md).

---

## 5. Split Calculation Logic: Four Modes via `split_type`

**Decision:** Represent all four split types (equal, unequal, percentage, share) through a single `split_type` field on `Expense`, with per-participant allocations stored on `ExpenseParticipant`.

**Rationale:**
- Single source of truth for "how was this expense divided"
- `ExpenseParticipant.share_amount` and `percentage` fields can represent any of the four modes without separate tables per split type

**Validation rules:**
- Percentage split: sum of percentages must equal 100
- Share split: allocation calculated proportionally from relative share values
- Unequal split: explicit amounts must sum to the expense total

**Status:** Implemented.

---

## 6. Anomaly Detection as a First-Class Concept

**Decision:** Treat CSV import anomalies as persisted records (`ImportAnomaly`) tied to an `ImportJob`, rather than just logging or rejecting bad rows silently.

**Rationale:**
- Produces an auditable import report (row number, issue type, action taken)
- Allows partial imports — valid rows proceed, problem rows are flagged rather than failing the whole batch

**Anomaly types covered:** missing payer, missing currency, unknown payer, unknown participant, settlement detection, duplicate expenses, membership violations, negative amounts, invalid percentage allocations.

**Status:** Implemented.

---

## 7. Deployment Target: Railway or Render

**Decision:** Target Railway or Render for deployment rather than AWS/GCP/Azure.

**Rationale:**
- Minimal configuration for Django apps
- Free/low-cost tiers suitable for an assignment deliverable
- Faster path to a public URL within the timeline

**Status:** Planned, not yet executed.

---
## 8. Deferred: Auth, Groups, Settlements, Real-Time Chat

**Decision:** Defer authentication, group management UI, settlement workflow, and real-time expense chat beyond the initial build window.

**Rationale:**
- Time was allocated first to data modeling, split logic, and CSV import/validation as the "core business logic" of the product
- These deferred items were judged as more standard CRUD/UI work, assumed to be addable once the data layer was stable

**Risk:** These four items map directly to assignment minimum requirements (login module, group management with invite/add/remove, settle debts/record payments, expense chat). Deferring them creates a gap against the stated minimum scope.

**Status:** Not implemented. Highest-priority remaining work.
