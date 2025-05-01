from sqlalchemy.orm import Mapped, mapped_column
from app import db

class Planet(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[str]


    def __init__(self, name: str, description: str, size: str):
        self.name = name
        self.description = description
        self.size = size

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }

