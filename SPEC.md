# Expense Tracker — Product Specification

## Problem

Users need a simple way to record their income and expenses and understand their current financial position without relying on spreadsheets or manual calculations.

The Expense Tracker will provide a clean, responsive web interface where a user can:

* Record income and expense transactions.
* Specify a category, amount, and date for each transaction.
* View all recorded transactions in chronological history.
* View automatically calculated total income, total expenses, and current balance.

The application is intended to demonstrate a complete CRUD-oriented web application using Flask, SQLite, HTML/CSS, and Bootstrap 5.

---

## Users

### Primary User

A single user managing their personal financial transactions on a local application.

### User Characteristics

The user should be able to use the application without technical knowledge of Flask, SQLite, or the underlying implementation.

### Authentication

Authentication is not required.

The application is intentionally scoped as a single-user local application for this assignment.

---

## Product Scope

The application consists of two primary areas:

1. **Dashboard / Transaction Entry**

   * Financial summary.
   * Form for adding transactions.

2. **Transaction History**

   * Table containing all recorded transactions.
   * Transaction details including date, type, category, and amount.

The application must persist transactions in SQLite so that data remains available after restarting the application.

---

## Functional requirements

- FR-1: The application MUST allow the user to add a financial transaction.
- FR-2: The transaction form MUST provide exactly two transaction types: Income and Expense.
- FR-3: The transaction form MUST require a category from a fixed set (Food, Transport, Utilities, Entertainment, Shopping, Miscellaneous).
- FR-4: The transaction form MUST require a numeric amount greater than 0.
- FR-5: The transaction form MUST require a transaction date.
- FR-6: All transaction fields MUST be mandatory and validated.
- FR-7: The application MUST display all stored transactions in a table.
- FR-8: The dashboard MUST display Total Income, Total Expense, and Current Balance.
- FR-9: Current Balance MUST be calculated as Total Income - Total Expense.
- FR-10: The financial summary MUST update automatically after a valid transaction is added.
- FR-11: All transactions MUST be stored in SQLite and persist across restarts.
- FR-12: The application MUST handle the empty state when no transactions exist.

---

## Non-functional requirements

- NFR-1: The application MUST provide a responsive interface using Bootstrap 5.
- NFR-2: The interface SHOULD provide clear labels, identification, validation messages, and consistent layout.
- NFR-3: Normal page loads and transaction submissions SHOULD complete without noticeable delay for the local dataset.
- NFR-4: The application MUST NOT create a database record when validation fails.
- NFR-5: The Flask application SHOULD separate configuration, database operations, routes, templates, and static assets.
- NFR-6: Forms MUST use descriptive labels; validation messages SHOULD be understandable without relying on color.
- NFR-7: Server-side validation MUST be performed; database queries MUST use parameterized queries to prevent SQL injection.


---

## Constraints

The application MUST use the following technology stack:

* Python
* Flask
* SQLite
* HTML
* CSS
* Bootstrap 5

### Backend

Flask MUST be used as the web framework.

### Database

SQLite MUST be used for persistent transaction storage.

No external database server is required.

### Frontend

HTML/CSS and Bootstrap 5 MUST be used for the user interface.

A frontend framework such as React is outside the required scope.

### Deployment

The application is intended to run locally for the assignment.

Cloud deployment is not required.

### External Services

The core application MUST NOT depend on external APIs or third-party financial services.

---

## Data Model

The application MUST maintain a transaction record containing at least:

| Field            | Type    | Required |
| ---------------- | ------- | -------- |
| id               | Integer | Yes      |
| transaction_type | String  | Yes      |
| category         | String  | Yes      |
| amount           | Numeric | Yes      |
| date             | Date    | Yes      |

The `id` MUST uniquely identify each transaction.

The application SHOULD use an auto-incrementing primary key for transaction IDs.

---

## Non-goals

The following features are explicitly outside the scope of this assignment:

* User registration.
* Login/logout.
* Multiple user accounts.
* Password management.
* Bank account synchronization.
* Automatic bank transaction imports.
* Receipt OCR.
* Receipt image uploads.
* Multi-currency support.
* Investment tracking.
* Monthly budget management.
* Financial forecasting.
* Advanced financial analytics.
* User-created category management.
* CSV/PDF export.
* Email notifications.
* Mobile native applications.
* Cloud infrastructure.
* Payment processing.
* Third-party financial APIs.

Charts and advanced analytics are also outside the minimum assignment scope.

---

## Acceptance criteria

- AC-1: The Flask application MUST start successfully.
- AC-2: Valid Income transactions MUST be saved to SQLite and appear in history.
- AC-3: Valid Expense transactions MUST be saved to SQLite and appear in history.
- AC-4: Invalid form submissions MUST NOT be saved and MUST display validation messages.
- AC-5: Zero, negative, or non-numeric amounts MUST be rejected.
- AC-6: Transaction history MUST display all stored transactions.
- AC-7: The dashboard MUST show correct Total Income, Total Expense, and Current Balance.
- AC-8: Balance must be calculated correctly as Total Income - Total Expense.
- AC-9: Financial summary MUST update automatically after new transaction submission.
- AC-10: Transactions MUST persist across application restarts.
- AC-11: Interface MUST remain usable across desktop, tablet, and mobile viewports.
- AC-12: Empty database state MUST show 0 totals and a "no transactions" message.


---

## Risks

### Risk 1: Incorrect Financial Calculations

**Risk:** Income and expense totals could be calculated incorrectly.

**Mitigation:** Calculate totals directly from persisted transaction records and test income, expense, and mixed transaction scenarios.

### Risk 2: Invalid Transaction Data

**Risk:** Invalid or incomplete values could be stored.

**Mitigation:** Perform server-side validation before database insertion.

### Risk 3: Data Loss

**Risk:** Transactions could disappear after application restart.

**Mitigation:** Persist transactions in SQLite rather than storing them only in application memory.

### Risk 4: SQL Injection

**Risk:** User-provided values could be inserted into SQL queries unsafely.

**Mitigation:** Use parameterized SQL queries or a safe database abstraction.

### Risk 5: Responsive Layout Issues

**Risk:** The interface could become difficult to use on smaller screens.

**Mitigation:** Use Bootstrap 5 responsive components and test common desktop and mobile viewport sizes.

### Risk 6: Scope Expansion

**Risk:** Additional features could consume development time and introduce unnecessary complexity.

**Mitigation:** Implement the documented functional and acceptance requirements first and keep authentication, analytics, exports, budgeting, and integrations outside the assignment scope.

---

## Open questions

No blocking product questions remain.

The following decisions are fixed for the assignment:

| Decision         | Choice                      |
| ---------------- | --------------------------- |
| User model       | Single-user                 |
| Authentication   | Not required                |
| Currency         | INR                         |
| Categories       | Fixed predefined categories |
| Database         | SQLite                      |
| Backend          | Flask                       |
| Frontend         | HTML/CSS + Bootstrap 5      |
| Charts           | Not required                |
| Budget tracking  | Not required                |
| Export           | Not required                |
| External APIs    | Not required                |
| Cloud deployment | Not required                |

