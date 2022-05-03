from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("website.config")

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy()
db.init_app(app)

from website.blueprints.main import main as main_blueprint

app.register_blueprint(main_blueprint)
from website.blueprints.auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

import website.views
import website.models

db.create_all(app=app)
