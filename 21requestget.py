from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
        return "GET request received!"

app.run(debug=True)