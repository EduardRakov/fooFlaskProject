from flask import Flask
from flask import request

app = Flask(__name__) #WSGI application


@app.route('/hello')
def hello():
    name = request.args.get('name')
    if not is_param_valid(name):
        return invalid_param_response()

    return "<h1>Hello, %s</h1>" % name


@app.route('/bye')
def bye():
    name = request.args.get('name')
    if not is_param_valid(name):
        return invalid_param_response()

    return "<h1>Goodbye, %s</h1>" % name


def is_param_valid(param):
    return param is not None and param is not ''


def invalid_param_response():
    return 'Param is empty or invalid', 400
