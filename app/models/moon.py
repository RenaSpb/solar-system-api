from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    orbit_period: Mapped[float] = mapped_column(nullable=True)
    planet_id: Mapped[int] = mapped_column(db.ForeignKey("planet.id"))
    planet: Mapped["Planet"] = relationship(back_populates="moons")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description,
            "orbit_period": self.orbit_period,
            "planet_id": self.planet_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            size=data["size"],
            description=data["description"],
            orbit_period=data["orbit_period"],
            planet_id=data["planet_id"]
        )