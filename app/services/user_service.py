from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import user_schema
from werkzeug.security import generate_password_hash
from app.exceptions.custom_exceptions import EmailAlreadyExistsError, UserNotFoundError, CustomValidationError
from marshmallow import ValidationError

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, data):
        try:
            user_data = user_schema.load(data)
        except ValidationError as err:
            raise CustomValidationError(err.messages)
        
        if self.repository.find_by_email(user_data.email):
            raise EmailAlreadyExistsError()

        hashed_pw = generate_password_hash(data['password'])

        return self.repository.create(
            username=user_data.username,
            email=user_data.email,
            password=hashed_pw
        )
    
    def get_users(self):
        users = self.repository.find_all()
        return users
    
    def get_user_by_id(self, id):
        user = self.repository.find_by_id(id)
        if not user:
            raise UserNotFoundError()

        return user