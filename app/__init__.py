from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_rbac import RBAC
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
rbac = RBAC()
login_manager = LoginManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    rbac.init_app(app)

    from .routes.main_route import main_route
    app.register_blueprint(main_route)

    return app
