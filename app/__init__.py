# app/__init__.py
from flask import Flask
from app.bot1 import bot1_bp
from app.todo import todo_bp
from app.bot2 import bot2_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints with URL prefixes
    app.register_blueprint(bot1_bp, url_prefix='/bot1')
    app.register_blueprint(todo_bp, url_prefix='/todo')
    app.register_blueprint(bot2_bp, url_prefix='/bot2')

    # Add a root route to avoid 404 on /
    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Flask app",
            "available_routes": ["/bot1", "/todo", "/bot2"]
        })

    return app
