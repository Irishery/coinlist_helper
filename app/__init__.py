from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()

def create_app(config):
    app = Flask(__name__)
    print(config)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.main_route import main_route
    app.register_blueprint(main_route)

    return app
