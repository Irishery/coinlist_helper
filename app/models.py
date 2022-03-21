from sqlalchemy.dialects.postgresql import JSON
from flask_rbac import UserMixin, RoleMixin
from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


roles_parents = db.Table(
    'roles_parents',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), 
                                     primary_key=True),
    db.Column('parent_id', db.Integer, db.ForeignKey('role.id'), 
                                       primary_key=True)
)


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    parents = db.relationship(
        'Role',
        secondary=roles_parents,
        primaryjoin=(id == roles_parents.c.role_id),
        secondaryjoin=(id == roles_parents.c.parent_id),
        backref=db.backref('children', lazy='dynamic')
    )

    def __init__(self, name, description):
        RoleMixin.__init__(self)
        self.name = name
        self.description = description

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_parents(self, *parents):
        for parent in parents:
            self.add_parent(parent)

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()


users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'),
                                     primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'),
                                     primary_key=True)
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    login = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cookie = db.Column(JSON)
    info = db.Column(db.String(255))
    proxy_host = db.Column(db.String(255))
    proxy_port = db.Column(db.String(255))
    proxy_login = db.Column(db.String(255))
    proxy_pass = db.Column(db.String(255))
    user_agent = db.Column(db.String(255))
    unmasked_vendor = db.Column(db.String(255))
    unmasked_renderer = db.Column(db.String(255))
    resolution = db.Column(db.String(255))
    last_enter = db.Column(db.DateTime(timezone=True), nullable=False)

    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('roles', lazy='dynamic')
    )

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

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        for role in self.roles:
            yield role


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
