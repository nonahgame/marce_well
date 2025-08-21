# app/__init__.py
from flask import Flask
from app.bot1.routes import bot1
from app.todo.routes import todo
from app.bot2.routes import bot2

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints with URL prefixes
    app.register_blueprint(bot1_bp, url_prefix='/bot1')
    app.register_blueprint(todo_bp, url_prefix='/todo')
    app.register_blueprint(bot2_bp, url_prefix='/bot2')


    return app


