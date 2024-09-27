from app.routes import app

if __name__ == "__main__":
    print("starting flask server.")
    app.run(debug=True, host='0.0.0.0', port=8080)