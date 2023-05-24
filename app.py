'''
flask 
'''

from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'


@app.route('/f1')
def f1():
    return 'f1'

@app.route('/f2')
def f2():
    time.sleep(0.5)
    return 'f2'