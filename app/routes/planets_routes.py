from flask import Blueprint, request, Response, jsonify
from app.models.planet import Planet
from ..db import db
from .route_utilities import validate_model

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict(), 200

@bp.post("")
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@bp.get("")
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

    planets_response = [planet.to_dict() for planet in planets]

    return planets_response

@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.size = request_body["size"]
    planet.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("/<planet_id>")
def delete_book(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.patch("/<planet_id>")
def update_part_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    if "name" in request_body:
        planet.name = request_body["name"]
    if "size" in request_body:
        planet.size = request_body["size"]
    if "description" in request_body:
        planet.description = request_body["description"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")



