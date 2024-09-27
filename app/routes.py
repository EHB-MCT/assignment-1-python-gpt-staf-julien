from flask import Flask, request, jsonify

# import controllers
from app.controllers.user_controller import UserController

app = Flask(__name__)

user_controller = UserController()

# GET request
@app.route('/helloworld')
def hello():
    """returns hello world"""
    return "Hello World!"

# POST request
@app.route('/helloworld', methods = ['POST'])
def hello_post():
    """returns 'Hello World!' in post."""
    return "Hello World! (POST)"

@app.route('/users', methods=['GET'])
def get_users():
    """Returns a list of users."""
    return user_controller.get_users()

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Returns a single user by ID."""
    return user_controller.get_user(user_id)

# only accepts json as req body
@app.route('/user/create',  methods=['POST'])
def create_user():
    """lets you create an user"""
    data = request.get_json()
    if data:
        return user_controller.create_user(data['name'], data['email']), 200
    else:
        return jsonify({"error": "Empty body"}), 400