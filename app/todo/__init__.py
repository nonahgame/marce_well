# app/todo/__init__.py
from flask import Blueprint

todo_bp = Blueprint('todo', __name__, template_folder='templates', static_folder='static', data_folder='data')

from . import routes