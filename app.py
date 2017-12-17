from flask import Flask, request, jsonify
from resources import *
from flask import make_response
from time import gmtime, strftime

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


@app.route('/api/v1/users', methods=['POST'])
def create_user():

    if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400)

    user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'name': request.json.get('name',""),
        'password': request.json['password']
    }

    return jsonify({'status': add_user(user)}), 201

@app.route('/api/v1/users', methods=['DELETE'])
def delete_user():

    if not request.json or not 'username' in request.json:
        abort(400)

    user=request.json['username']

    return jsonify({'status': del_user(user)}), 200

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    user = {}
    # if not request.json:
    #     abort(400)

    user['id']=user_id
    key_list = request.json.keys()

    for i in key_list:
        user[i] = request.json[i]

    print (user)

    return jsonify({'status': upd_user(user)}), 200

@app.route('/api/v2/tweets', methods=['GET'])
def get_tweets():
    return list_tweets()

@app.route('/api/v2/tweets', methods=['POST'])
def add_tweets():

    user_tweet = {}

    if not request.json or not 'username' in request.json or not 'body' in request.json:
        abort(400)

    user_tweet['username'] = request.json['username']
    user_tweet['body'] = request.json['body']
    user_tweet['created_at']=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())

    print (user_tweet)

    return  jsonify({'status': add_tweet(user_tweet)}), 201

@app.route('/api/v2/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    return list_tweet(id)


app.run(host='0.0.0.0', port=5000, debug=True)
