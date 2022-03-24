from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_authorize import Authorize


db = SQLAlchemy()
migrate = Migrate()
authorize = Authorize()
login_manager = LoginManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_manager.login_view = "auth.sign_in"
    login_manager.init_app(app)
    authorize.init_app(app)
    migrate.init_app(app, db)

    from .routes.auth import auth_route
    from .routes.main import main_route
    app.register_blueprint(auth_route)
    app.register_blueprint(main_route)

    from app.api.user_api import user_api
    app.register_blueprint(user_api)

    return app
