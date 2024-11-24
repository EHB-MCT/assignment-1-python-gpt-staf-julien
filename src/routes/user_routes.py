from pydantic import ValidationError
from src.repositories.user_repository import UserRepository
from flask import jsonify, Blueprint, request
from schemas.user_schema import CreateUserRequest, UpdateUserRequest

user_service = UserRepository()

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
    """Create a new user with name and email."""
    try:
        # Parse and validate the incoming JSON request
        data = request.get_json()
        validated_data = CreateUserRequest(**data)
    except ValidationError as e:
        # Return validation errors in case of invalid data
        return jsonify({"errors": e.errors()}), 400
    except Exception as e:
        # Handle missing or malformed JSON
        return jsonify({"error": str(e)}), 400

    # Use the validated data to create a user
    user = user_service.create_user(validated_data.name, validated_data.email)
    return jsonify(user), 201

@user_controller_bp.route('/user/update', methods=['PUT'])
def update_user():
    """Update a user's name and/or email by ID."""
    try:
        # Parse and validate the incoming JSON request
        data = request.get_json()
        validated_data = UpdateUserRequest(**data)
    except ValidationError as e:
        # Return validation errors in case of invalid data
        return jsonify({"errors": e.errors()}), 400
    except Exception as e:
        # Handle missing or malformed JSON
        return jsonify({"error": str(e)}), 400

    # Perform the update using the validated data
    user = user_service.update_user(
        validated_data.user_id, 
        validated_data.name, 
        validated_data.email
    )

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
