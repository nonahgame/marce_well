# app/bot2/__init__.py
from flask import Blueprint

bot2_bp = Blueprint('bot2', __name__, template_folder='templates', static_folder='static', data_folder='data')

from . import routes