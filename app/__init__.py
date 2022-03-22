from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_rbac import RBAC
from flask_login import LoginManager, current_user
from flask_restful import Api


db = SQLAlchemy()
migrate = Migrate()
rbac = RBAC()
login_manager = LoginManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    # app.json_encoder = CustomJSONEncoder  
    
    api = Api(app)

    db.init_app(app)
    login_manager.login_view = "auth.sign_up"
    login_manager.init_app(app)
    migrate.init_app(app, db)

    rbac.set_user_loader(lambda: current_user)
    rbac.init_app(app)


    from .routes.auth import auth_route
    from .routes.main import main_route
    app.register_blueprint(auth_route)
    app.register_blueprint(main_route)

    from app.api.user_api import UserApi
    api.add_resource(UserApi, '/users/<int:id>')

    return app
