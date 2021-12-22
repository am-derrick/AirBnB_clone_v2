#!/usr/bin/python3
"""
contains the class DBStorage
"""

from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """Represenataion of DBStorage class"""
    __engine = None
    __session = None

    def __int__(self):
        """Instantiates a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNB_MYSQL_DB,
                                             pool_pre_ping=True))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """query on database sessionn"""
        dict_new = {}
        for clas in classes:
            if cls is None or cls is classes[clas] or cls is clas:
                objs = self.__session.query(classes[clas]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to current database session"""
         self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from database"""
        Base.metadata.create_all(self.__engine)
        session_make = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_make)
        self.__session = Session
