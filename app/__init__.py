import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

db      = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_TEST_DATABASE_URI")
        
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI") or "postgresql+psycopg2://localhost/solar_system_development"

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.planets_routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
