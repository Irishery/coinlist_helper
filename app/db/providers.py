from flask_sqlalchemy import SQLAlchemy
from ..main.manager import app
from flask_migrate import Migrate


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pas277@localhost:5432/"
METADATA = SQLAlchemy.metadata
db = SQLAlchemy(app)

migrate = Migrate(app, db)
