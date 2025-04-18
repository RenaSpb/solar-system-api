from flask import Blueprint, abort, make_response
from app.models.planet import planets, Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_books():
    planets_response = [planet.to_dict() for planet in planets]
    return planets_response

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size" : planet.size
    }, 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))
        
    for planet in planets:
        if planet.id == planet_id:
            return planet
        
    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))