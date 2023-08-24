from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Task 2 complete !!!'
