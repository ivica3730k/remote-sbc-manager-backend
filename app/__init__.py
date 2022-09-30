from flask_restx import Api
from flask import Blueprint

from .main.controller.file_controller import api as file_ns


blueprint = Blueprint('api', __name__)


api = Api(blueprint,
          title='Remote SBC Manager Backend',
          version='1.0',
          description='Remote SBC Manager Backend',)


api.add_namespace(file_ns, path='/file')

