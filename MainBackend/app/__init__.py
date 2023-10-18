from flask import Flask
import os
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from config import config_options
from dotenv import load_dotenv
from flask_simplemde import SimpleMDE
import os

db = SQLAlchemy()
migrate = Migrate()

ma = Marshmallow()
load_dotenv()

simple = SimpleMDE()
def create_app(config_name):

    app = Flask(__name__)


    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
   
    CORS(app)
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

   
    app.config['SQLALCHEMY_POOL_SIZE'] = 5
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800


    with app.app_context():
        db.create_all()

    from .transactions import transactions as transactions_blueprint
    app.register_blueprint(transactions_blueprint)
    return app
