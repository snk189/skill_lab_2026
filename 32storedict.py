from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage
users = {
    "admin": "1234",
    "satya": "abcd"
}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users and users[username] == password:
        return "Login successful!"

    return "Invalid username or password!"

app.run(debug=True)