# app/bot1/__init__.py
from flask import Blueprint

bot1_bp = Blueprint('bot1', __name__, template_folder='templates', static_folder='static', data_folder='data')

from . import routes