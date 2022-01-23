import os
import subprocess
import sys
from flask import redirect, url_for
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.extensions import db

app = create_app(os.environ.get('FLASK_ENV', default='development'))
app.app_context().push()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():

    @app.route('/')
    def docs():
        return redirect(url_for('blueprint_v1.index'), code=302)

    app.run()


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


class Pytest(Command):
    """Run tests with pytest."""
    name = "pytest"
    capture_all_args = True

    def run(self, argv):
        if sys.platform == 'linux' or sys.platform == 'linux2':
            ret = subprocess.call(
                ['venv/bin/pytest',
                 '--cov=app',
                 '--cov-report=term-missing',
                 ] + argv)
            sys.exit(ret)
        elif sys.platform == 'win32':
            ret = subprocess.call(
                ['venv/Scripts/pytest.exe',
                 '--cov=app',
                 '--cov-report=term-missing',
                 ] + argv)
            sys.exit(ret)
        else:
            ret = subprocess.call(
                ['venv/bin/pytest',
                 '--cov=app',
                 '--cov-report=term-missing',
                 ] + argv)
            sys.exit(ret)



manager.add_command('pytest', Pytest())


if __name__ == '__main__':
    manager.run()
