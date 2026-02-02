from app.extensions import ma
from app.models.user_model import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        ordered = True
        exclude = ("password",)

user_schema = UserSchema()
users_schema = UserSchema(many=True)