from app.views import app
import logging

app.config['DEBUG']

logging.basicConfig(filename="flask_server.log", level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting Flask Server")
    app.run(debug=True, host='0.0.0.0', port=8080)