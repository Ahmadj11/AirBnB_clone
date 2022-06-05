#!/usr/bin/python3
"""BaseModel class module that all AirBnB classes will inherit from"""


import json
import uuid
from datetime import datetime
import time

class BaseModel:
    """Defines all common attributes & methods for AirBnB classes"""
    def __init__(self):
        """"instantiation which defines our public instance attributes"""
        id =  str(uuid.uuid4())  # generates
        self.id = id
        created_at = datetime.now()
        self.created_at = created_at
        self.updated_at = created_at

    def __str__(self):
        """overwriting __str__ method to print object how we would like"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """update updated_at attr w/ current date time"""
        currentdt = datetime.now()
        self.updated_at = currentdt

    def to_dict(self):
        """create & return dictionary of instance attributes"""
        newdict = self.__dict__
        newdict['__class__'] = self.__class__.__name__
        newdict['updated_at'] = self.updated_at.isoformat()
        newdict['id'] = self.id
        newdict['created_at'] = self.created_at.isoformat()
        return newdict
