from flask import Flask

from .commands import create_tables
from .extensions import db, login_manager
from .models import doctors
from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    app.secret_key = 'alskjdfald;afj'

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = 'main.login'

    @login_manager.user_loader
    def load_user(user_id):
        return doctors.query.get(user_id)

    app.register_blueprint(main)

    app.cli.add_command(create_tables)

    return app
