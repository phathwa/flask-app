from flask import Flask
from .config import Config
from .extensions import db, migrate, bcrypt, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .main.route import main
    from .users.routes import users
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
