from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.schemas.user_schema import users_schema

user_bp = Blueprint('users', __name__)
user_service = UserService()

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Validação de campos
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Dados incompletos"}), 400

    result, status_code = user_service.create_user(data)
    return jsonify(result), status_code

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_users()
    
    return users_schema.jsonify(users), 200

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    
    return users_schema.jsonify(user), 200
