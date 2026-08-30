from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
        return "POST request received!"

app.run(debug=True)