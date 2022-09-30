#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_restx import Namespace, fields
from werkzeug.datastructures import FileStorage


class FileDto:

    api = Namespace('files', description='File upload related operations')
    upload_parser = api.parser()
    upload_parser.add_argument('file',
                               location='files',
                               type=FileStorage,
                               required=True)
