#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

store_t = getenv("HBNB_TYPE_STORAGE")

if store_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
