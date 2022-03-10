from flask import Flask
from db.providers import migrate
from app.main.main_route import main_route

app = Flask(__name__)

app.register_blueprint(main_route)


if __name__ == "__main__":
    migrate.init()
    app.run(debug=True)
