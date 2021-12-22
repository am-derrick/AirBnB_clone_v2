#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ Review class to store review information """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nulable=False, ForeignKey(places.id))
        user_id = Column(String(60), nullable=False, ForeignKey(users.id))
    else:
        place_id = ""
        user_id = ""
        text = ""
