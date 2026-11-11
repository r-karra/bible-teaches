import os
from flask import Flask
from extensions import db, login_manager
from models import User

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'f5eda6832c4b48e1d075bc6bd64f0a065ca6e2d2c0c31544bac63e7463197232')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # User loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints
    from routes.home import home_bp
    from routes.auth import auth_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app
