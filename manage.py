import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.extensions import db

app = create_app(os.environ.get('FLASK_ENV'))
app.app_context().push()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def drop_tables():
    """Drop tables if they exist."""
    print('Dropping tables...')
    db.drop_all()
    print('Tables destroyed.')


@manager.command
def create_tables():
    """Create tables if they do not exist."""
    print('Creating tables...')
    db.create_all()
    print('Tables created successfully.')


if __name__ == '__main__':
    manager.run()
