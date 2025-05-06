from flask import Blueprint, request, abort, make_response, Response
from app.models.moon import Moon
from app.models.planet import Planet
from ..db import db
from .route_utilities import validate_model, create_model

bp = Blueprint("moons_bp", __name__, url_prefix="/planets")


@bp.post("/<planet_id>/moons")
def create_moon(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    request_body["planet_id"] = planet.id
    return create_model(Moon, request_body), 201


@bp.get("/<planet_id>/moons")
def get_all_moons(planet_id):
    planet = validate_model(Planet, planet_id)
    moons = [moon.to_dict() for moon in planet.moons]
    return moons, 200

@bp.delete("/<planet_id>/moons/<moon_id>")
def delete_moon(planet_id, moon_id):
    validate_model(Planet, planet_id) 
    moon = validate_model(Moon, moon_id)  

    db.session.delete(moon)
    db.session.commit()

    return Response(status=204, mimetype="application/json")