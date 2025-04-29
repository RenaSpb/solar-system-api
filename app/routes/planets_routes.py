from flask import Blueprint, abort, make_response, request, Response, jsonify
from app.models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size" : planet.size
    }, 200

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    size = request_body["size"]

    new_planet = Planet(name=name, description=description, size=size)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "size": new_planet.size,
    }
    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    size_param = request.args.get("size")
    if size_param:
        query = query.where(Planet.size.ilike(f"%{size_param}%"))

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "size": planet.size,
            }
        )

    return jsonify(planets_response)

# http://127.0.0.1:5000/planets
# http://127.0.0.1:5000/planets?description=test
# http://127.0.0.1:5000/planets?size=small
# http://127.0.0.1:5000/planets?size=small&description=test

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.size = request_body["size"]
    planet.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<planet_id>")
def delete_book(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.patch("/<planet_id>")
def update_part_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    if "name" in request_body:
        planet.name = request_body["name"]
    if "size" in request_body:
        planet.size = request_body["size"]
    if "description" in request_body:
        planet.description = request_body["description"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))
        
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))

    return planet
