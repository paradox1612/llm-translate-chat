# app/main.py
# Create a Flask application that initializes routes from app.routes and runs on host '0.0.0.0' and port 5000.
from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__)
    init_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
