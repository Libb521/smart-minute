from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from .config import config_options


# Initializing application
# bootstrap.init_app(app)
app = Flask(__name__)


#setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error

from app import views
from app import error