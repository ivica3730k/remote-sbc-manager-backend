from flask import current_app
from ..custom_exceptions import *
import os


def save_file(file, filename, folder=""):
    if folder:
        folder = f"./uploads/{folder}"
    else:
        folder = "./uploads"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = f"{folder}/{filename}"
    if _does_file_exist(filepath):
        raise FileAlreadyExistsError(f"File {filepath} already exists")
    file.save(filepath)
    return filepath


def _does_file_exist(filepath):
    return os.path.exists(filepath)
