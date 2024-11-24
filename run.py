from app import create_app
import logging
import config

logging.basicConfig(filename="flask_server.log", level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting Flask Server")
    app = create_app() # create and register blueprints
    app.run(debug=True, host='0.0.0.0', port=config.PORT)