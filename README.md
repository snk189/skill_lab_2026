# Flask Basics – Workshop

This repository contains the Flask concepts covered in the workshop, taught step-by-step through small examples.

## Flow

1. Basic Flask Application
2. Routing
3. Multiple Routes
4. Dynamic Routes
5. GET Requests
6. POST Requests
7. HTML Forms
8. GET vs POST
9. Form `method` and `action`
10. Receiving Form Data with `request.form`
11. Rendering HTML with `render_template`
12. Basic Validation
13. Temporary Storage using Python Dictionary
14. SQLite Database
15. INSERT Data
16. SELECT Data
17. Using SQLite for Login Authentication

## Final Flow

```text
HTML Form
    ↓
POST Request
    ↓
Flask Route
    ↓
request.form
    ↓
SQLite
    ↓
Find User
    ↓
Check Credentials
    ↓
Login Success / Failure
```

## Setup

Install Flask:

```bash
pip install flask
```

Run any Flask example:

```bash
python filename.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Note

The examples are intentionally kept simple and are meant for learning Flask fundamentals. They are not production-ready authentication implementations.
