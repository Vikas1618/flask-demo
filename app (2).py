from flask import Flask
app = Flask(__name__)

@app.route("/flask-demo")
def hello():
    return "Hello, World!"
