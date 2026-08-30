from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("users.db")

    result = conn.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

    user = result.fetchone()
    conn.close()

    if user and user[1] == password:
        return "Login successful!"

    return "Invalid username or password!"

app.run(debug=True)