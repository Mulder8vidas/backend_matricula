from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import loginController
from . import matriculaController
from . import alumnosController
from . import AulasController