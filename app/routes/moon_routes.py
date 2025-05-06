from flask import Blueprint, request, abort, make_response, Response
from app.models.moon import Moon
from app.models.planet import Planet
from ..db import db
from .route_utilities import validate_model

bp = Blueprint("moons_bp", __name__, url_prefix="/planets")


@bp.post("/<planet_id>/moons")
def create_moon(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    try:
        new_moon = Moon.from_dict(request_body)
    except KeyError as e:
        response = {"message": f"Missing {e.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_moon)
    db.session.commit()

    return new_moon.to_dict(), 201


@bp.get("/<planet_id>/moons")
def get_all_moons(planet_id):
    planet = validate_model(Planet, planet_id)
    moons = [moon.to_dict() for moon in planet.moons]
    return moons, 200
