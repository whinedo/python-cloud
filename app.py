from flask import Flask, request, jsonify
from resources import *
from flask import make_response

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(error):
    return make_response(
        jsonify({'error': 'Resource not found!'}), 404)

@app.route("/api/v1/info")
def info():
    return home_index()

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return list_user(user_id)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return list_users()

app.run(host='0.0.0.0', port=5000, debug=True)
