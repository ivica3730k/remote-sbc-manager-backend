from flask import request
from flask_restx import Resource
from werkzeug.utils import secure_filename

from ..service.file_service import *
from ..util.dto import FileDto
from ..custom_exceptions import *

api = FileDto.api


# create / endpoint
@api.route('/')
class FileUpload(Resource):

    @api.doc(description="Upload file")
    @api.response(200, "File stored successfully")
    @api.response(409, "File already exists")
    @api.expect(FileDto.upload_parser)
    def post(self):
        args = FileDto.upload_parser.parse_args()
        file = args["file"]

        filename = secure_filename(file.filename)
        try:
            result = save_file(file, filename)
            return {"message": f"Saved file {result}"}, 200
        except FileAlreadyExistsError as e:
            return {"message": str(e)}, 409

    @api.doc(description="Get all stored files")
    @api.response(200, "Files retrieved successfully")
    def get(self):
        return get_stored_files(), 200


@api.route('/iso')
class FileUpload(Resource):

    @api.doc(description="Upload file")
    @api.response(200, "File stored successfully")
    @api.response(409, "File already exists")
    @api.expect(FileDto.upload_parser)
    def post(self):
        args = FileDto.upload_parser.parse_args()
        file = args["file"]

        filename = secure_filename(file.filename)
        try:
            result = save_file(file, filename, "iso")
            return {"message": f"Saved file {result}"}, 200
        except FileAlreadyExistsError as e:
            return {"message": str(e)}, 409
