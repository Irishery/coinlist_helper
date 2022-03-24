from sqlalchemy.dialects.postgresql import JSON
from dataclasses import dataclass
from flask_login import UserMixin
from flask_authorize import AllowancesMixin
from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model, AllowancesMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description


UserRole = db.Table(
    'user_role', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


@dataclass
class User(db.Model, UserMixin):
    id: int = db.Column(db.Integer, primary_key=True)
    platform: str = db.Column(db.String(255), nullable=False)
    name: str = db.Column(db.String(255), nullable=False)
    login: str = db.Column(db.String(255), unique=True, nullable=False)
    password: str = db.Column(db.String(255), nullable=False)
    cookie: dict = db.Column(JSON)
    info: str = db.Column(db.String(255))
    proxy_host: str = db.Column(db.String(255))
    proxy_port: str = db.Column(db.String(255))
    proxy_login: str = db.Column(db.String(255))
    proxy_pass: str = db.Column(db.String(255))
    user_agent: str = db.Column(db.String(255))
    unmasked_vendor: str = db.Column(db.String(255))
    unmasked_renderer: str = db.Column(db.String(255))
    resolution: str = db.Column(db.String(255))
    last_enter: datetime = db.Column(db.DateTime(timezone=True), nullable=False)

    roles = db.relationship('Role', secondary=UserRole)

    def __init__(self, platform=None, name=None, login=None, password=None,
                 last_enter=datetime.now()):
        if platform:
            self.platform = platform
        if name:
            self.name = name
        if login:
            self.login = login
        if password:
            self.set_password(password)

        self.last_enter = last_enter
    
    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def add_role(self, role):
        self.roles.append(role)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
