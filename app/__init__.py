from flask import Flask
from flask_login import LoginManager,current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config_options

# from config import Config
app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
# added this line fixed the issue
login_manager.init_app(app)
bootstrap = Bootstrap()
mail = Mail(app)
login_manager.login_view = 'users.login'
login_manager.session_protection = 'strong'


def create_app(config_name):

    app = Flask(__name__)
    db.init_app(app)


    with app.app_context():
        db.create_all()
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    
    return app