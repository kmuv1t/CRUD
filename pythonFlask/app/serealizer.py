from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Book, User

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True

    livro = fields.Str(required=True)
    escritor = fields.Str(required=True)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Não envie pelo amor de deus o ID')


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    username = fields.Str(required=True)
    password = fields.Str(required=True)