from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import Optional

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[str]
    moons: Mapped[Optional[list["Moon"]]] = relationship(back_populates="planet")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }
    
        
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
                name=planet_data["name"],
                description=planet_data["description"],
                size=planet_data["size"]
        )