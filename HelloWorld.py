from flask import Flask, request, jsonify

app = Flask(__name__) # WSGI application

@app.route('/hello')
def hello():
    return prepared_response("Hello")

@app.route('/bye')
def bye():
    return prepared_response("Goodbye")

def prepared_response(message):
    name = request.args.get('name')
    if not name:
        return invalid_param_response()

    result = "{0} {1}".format(message, name)
    if request_wants_json():
        return jsonify({'message': result})

    if request_wants_text():
        return result

    return "<h1>{0} {1}</h1>".format(message, name)

def invalid_param_response():
    return 'Param is empty or invalid', 400

def request_wants_json():
    best = request.accept_mimetypes.best_match(['application/json', 'text/html'])
    return best == 'application/json' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']

def request_wants_text():
    best = request.accept_mimetypes.best_match(['text/plain', 'text/html'])
    return best == 'text/plain' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']
