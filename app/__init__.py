from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


# Initializing application
# bootstrap.init_app(app)
app = Flask(__name__)


#setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views