from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, welcome to my Flask App</h1>'