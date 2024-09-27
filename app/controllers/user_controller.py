from app.services.user_service import UserService
from flask import jsonify

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def get_user(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({"error": "User not found"}), 404

    def get_users(self):
        users = self.user_service.get_all_users()
        return jsonify(users), 200
