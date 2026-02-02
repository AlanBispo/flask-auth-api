from app.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, data):
        if self.repository.find_by_email(data['email']):
            return {"error": "E-mail já cadastrado"}, 400

        hashed_pw = generate_password_hash(data['password'])

        user = self.repository.create(
            username=data['username'],
            email=data['email'],
            password=hashed_pw
        )

        return {"id": user.id, "message": "Usuário criado com sucesso!"}, 201
    
    def get_users(self):
        users = self.repository.find_all()

        return users