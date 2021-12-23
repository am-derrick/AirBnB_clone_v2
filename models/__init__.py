#!/usr/bin/python3
<<<<<<< HEAD
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
=======
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

store_t = getenv("HBNB_TYPE_STORAGE")

if store_t == "db":
    storage = DBStorage()
else:
>>>>>>> ebe09c5eae79e587efce1d62062a6740d55447a1
    storage = FileStorage()
storage.reload()
