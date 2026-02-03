from app.extensions import ma
from app.models.user_model import UserModel
from marshmallow import fields, validate, ValidationError

def validate_not_admin(value):
    if value.lower() == 'admin':
        raise ValidationError("O nome de usuário 'admin' é proibido.")

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_fk = True
        exclude = ("password",)

    username = fields.String(
        required=True, 
        validate=[
            validate.Length(min=3, max=50, error="O nome deve ter entre 3 e 50 caracteres."),
            validate_not_admin
        ]
    )
    
    email = fields.Email(
        required=True, 
        error_messages={"invalid": "Formato de e-mail inválido."}
    )

    password = fields.String(
        required=True, 
        load_only=True, 
        validate=[validate.Length(min=8, error="A senha deve ter pelo menos 8 caracteres.")]
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)