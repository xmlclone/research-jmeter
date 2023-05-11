from flask import Flask

app = Flask(__name__)


@app.route('/<int:id>')
def index(id):
    return f'{id}'