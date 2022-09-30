from flask import current_app
from ..custom_exceptions import *
from collections import defaultdict
import glob
import json
import os
from os import path


def save_file(file, filename, folder=None):
    if folder is not None:
        folder = f"./files/{folder}"
    else:
        folder = "./files/uploads"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = f"{folder}/{filename}"
    if _does_file_exist(filepath):
        raise FileAlreadyExistsError(f"File {filepath} already exists")
    file.save(filepath)
    return filepath


def _does_file_exist(filepath):
    return os.path.exists(filepath)


def get_stored_files():
    base_path = "./files"
    d = defaultdict(list)

    for file in glob.iglob(path.join(base_path, '*/*'), recursive=True):
        d[path.basename(path.dirname(file))].append(path.basename(file))

    return d

