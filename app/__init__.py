from flask import Flask

# importing the blueprints from the respective modules
from .controllers.user_controller import user_controller_bp
from .views import user_bp

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] 
    app.config['DEBUG']

    # Initialize controllers, extensions, etc.
    app.register_blueprint(user_bp)
    app.register_blueprint(user_controller_bp)

    return app
