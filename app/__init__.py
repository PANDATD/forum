from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()



def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "..", "forum.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev_secret_key"


    db.init_app(app)

    # Import routes
    from .routes import main
    app.register_blueprint(main)

    return app
