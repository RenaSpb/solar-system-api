from app import create_app, db
from app.models.planet import Planet

my_app = create_app()

with my_app.app_context():
    db.session.add_all([
        Planet(name="Mercury", description="Closest to the Sun", size="small"),
        Planet(name="Venus", description="Thick toxic atmosphere", size="medium"),
        Planet(name="Earth", description="Home to humans and life", size="medium"),
        Planet(name="Mars", description="Red and dusty", size="small"),
        Planet(name="Jupiter", description="Gas giant with a big red spot", size="giant"),
        Planet(name="Saturn", description="Known for its rings", size="giant"),
        Planet(name="Uranus", description="Rotates on its side", size="large"),
        Planet(name="Neptune", description="Blue and windy", size="large"),
        Planet(name="Pluto", description="Dwarf planet with a heart-shaped plain", size="tiny"),
        Planet(name="Kepler-22b", description="Exoplanet in habitable zone", size="unknown")
    ])
    db.session.commit()
