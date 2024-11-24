from flask import Flask

# importing the blueprints from the respective modules
from .controllers.user_controller import user_controller_bp
from .routes.static_routes import user_bp

def create_app():
    """
    Create a Flask application instance and register the blueprints.
    
    return: 
        Flask application instance with blueprints registered.
    """
    app = Flask(__name__)

    app.config['SECRET_KEY'] 
    app.config['DEBUG']

    # Initialize controllers, extensions, etc.
    app.register_blueprint(user_bp)
    app.register_blueprint(user_controller_bp)

    return app
