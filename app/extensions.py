# app/extensions.py

# Import necessary classes from Flask extensions
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy for database ORM
from flask_migrate import Migrate         # Migrate for handling database migrations
from flask_login import LoginManager      # LoginManager for user session management
from flask_wtf import CSRFProtect         # CSRFProtect for Cross-Site Request Forgery protection
from flask_bcrypt import Bcrypt

# Initialize instances of the extensions
db = SQLAlchemy()  # Create an instance of SQLAlchemy for ORM functionality
migrate = Migrate()  # Create an instance of Migrate for database migration management
login_manager = LoginManager()  # Create an instance of LoginManager for user authentication
csrf = CSRFProtect()  # Create an instance of CSRFProtect to enable CSRF protection
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
