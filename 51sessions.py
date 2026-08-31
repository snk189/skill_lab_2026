from flask import Flask, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/login")
def login():
    session["user"] = "admin"
    return "Logged in!"

@app.route("/home")
def home():
    if "user" in session:
        return f"Welcome {session['user']}"
    return "Please login first"

@app.route("/logout")
def logout():
    session.clear()
    return "Logged out!"

app.run(debug=True)