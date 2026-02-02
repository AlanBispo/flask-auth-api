from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

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


