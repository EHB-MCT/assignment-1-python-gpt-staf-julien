from flask import Blueprint, request, jsonify

user_bp = Blueprint('users', __name__, url_prefix='/users')

# GET request
@user_bp.route('/helloworld')
def hello():
    """returns hello world"""
    return "Hello World!"

# POST request
@user_bp.route('/helloworld', methods = ['POST'])
def hello_post():
    """returns 'Hello World!' in post."""
    return "Hello World! (POST)"