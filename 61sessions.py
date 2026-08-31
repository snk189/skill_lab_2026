from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "1234":
        session["user"] = username
        return redirect("/home")

    return "Invalid username or password"

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")

    return render_template("home.html", username=session["user"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.run(debug=True)