from . import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Transcations(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100))
    amount = db.Column(db.String(255))

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
