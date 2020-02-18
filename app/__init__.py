from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from .config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Initializing application
    # bootstrap.init_app(app)
    app = Flask(__name__)


    #setting up configuration
    app.config.from_object(DevConfig)

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app