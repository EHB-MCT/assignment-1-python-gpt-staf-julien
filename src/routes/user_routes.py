from src.services.user_service import UserService
from flask import jsonify, Blueprint, request

user_service = UserService()

user_controller_bp = Blueprint('user', __name__)

@user_controller_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Return user data by id"""
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_controller_bp.route('/users', methods=['GET'])
def get_users():
    """Returns all user data"""
    users = user_service.get_all_users()
    return jsonify(users), 200

# only accepts json as req body
@user_controller_bp.route('/user/create',  methods=['POST'])
def create_user():
    """Create a new user with name and email"""
    data = request.get_json()

    name = data['name']
    email = data['email']

    # required fields
    if not name or not email:
        return jsonify({"error": "Missing required fields"}), 400

    # required fields
    user = user_service.create_user(name, email)
    return user

@user_controller_bp.route('/user/update', methods=['PUT'])
def update_user():
    """Update a user their name and email by id"""
    data = request.get_json()

    user_id = data['user_id']

    name = data.get('name')
    email = data.get('email')

    # required fields
    if not user_id:
        return jsonify({"error": "Missing required field 'user_id'"}), 400
    # required fields
    if not name and not email:
        return jsonify({"error": "No data to update"}), 400
    
    user = user_service.update_user(user_id, name, email)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_controller_bp.route('/user/delete', methods=['DELETE'])
def delete_user():
    """Delete a user by id"""
    data = request.get_json()

    user_id = data['user_id']

    # required fields
    if not user_id:
        return jsonify({"error": "No user id provided"}), 400
    
    result = user_service.delete_user(user_id)
    if result:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not deleted"}), 404
