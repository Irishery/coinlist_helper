import os
from app import db,  create_app
from app.models import User, Role
from dotenv import load_dotenv
# from flask_script import Manager, Shell
# from flask_migrate import MigrateCommand

load_dotenv()

app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopementConfig')
app.debug = True
# manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User)

def init_roles():
    user = Role('user', 'Have access to all data instead passwords')
    admin = Role('admin', 'Have access to all data')
    db.session.add(user)
    db.session.add(admin)
    db.session.commit()


# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # uncomment it to first start
    # with app.app_context():
        # init_roles()
    app.run(debug=True)
