from .models import *
from . import ma


# Trans schema for serialization
class TransSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transcations
