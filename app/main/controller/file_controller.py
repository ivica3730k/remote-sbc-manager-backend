from flask import request
from flask_restx import Resource
from werkzeug.utils import secure_filename

from ..service.file_service import *
from ..util.dto import FileDto

api = FileDto.api

