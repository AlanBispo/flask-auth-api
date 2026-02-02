from app.models.user_model import UserModel
from app.extensions import db

class UserRepository:
    def create(self, username, email, password):
        user = UserModel(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def find_all(self):
        return UserModel.query.all()
