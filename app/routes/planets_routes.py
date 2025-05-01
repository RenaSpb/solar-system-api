from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    size_param = request.args.get("size")
    description_param = request.args.get("description")

    query = Planet.query

    if size_param:
        query = query.where(Planet.size.ilike(f"%{size_param}%"))

    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    planets = query.all()
    result = [planet.to_dict() for planet in planets]
    return jsonify(result)


# 在 planets_routes.py add GET
@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return make_response({"error": f"Invalid planet id '{planet_id}'"}, 400)
    
    planet = Planet.query.get(planet_id)
    if planet:
        return planet.to_dict(), 200
    return make_response({"error": f"Planet with id {planet_id} not found"}, 404)

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return make_response({"error": f"Invalid planet id '{planet_id}'"}, 400)
    
    planet = Planet.query.get(planet_id)
    if not planet:
        return make_response({"error": f"Planet with id {planet_id} not found"}, 404)
    
    request_data = request.get_json()
    planet.name = request_data.get("name", planet.name)
    planet.description = request_data.get("description", planet.description)
    planet.size = request_data.get("size", planet.size)

    db.session.commit()

    return jsonify({"message": f"Planet {planet_id} successfully updated"}), 200

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    
    try:
        planet_id = int(planet_id)
    except ValueError:
        return make_response({"error": f"Invalid planet id '{planet_id}'"}, 400)
    
    planet = Planet.query.get(planet_id)
    if not planet:
        return make_response({"error": f"Planet with id {planet_id} not found"}, 404)
    
    db.session.delete(planet)
    db.session.commit()

    return jsonify({"message": f"Planet {planet_id} successfully deleted"}), 200

    
@planets_bp.post("")
def create_planet():
    request_data = request.get_json()

    try:
        new_planet = Planet(
            name=request_data["name"],
            description=request_data["description"],
            size=request_data["size"]
        )
    except KeyError as e:
        return make_response({"error": f"Missing field: {e}"}, 400)

    db.session.add(new_planet)
    db.session.commit()

    res = jsonify({"message": f"Planet {new_planet.name} created", "id": new_planet.id})
    return res, 201
