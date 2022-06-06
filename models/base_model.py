#!/usr/bin/python3
"""BaseModel class module that all AirBnB classes will inherit from"""


import json
import uuid
from datetime import datetime
import time
# first step in linking BaseModel to FileStorage through variable storage
from models.__init__ import storage


class BaseModel:
    """Defines all common attributes & methods for AirBnB classes"""
    def __init__(self, *args, **kwargs):
        """"instantiation which defines our public instance attributes"""
        # list to protect from invalid keywords
        valid_attr = ['id', 'created_at', 'updated_at']
        # variable to help convert str back to datetime object
        formatcode = "%Y-%m-%dT%H:%M:%S.%f"
        # creating new instance attr first because kept getting error about id
        id = str(uuid.uuid4())
        self.id = id
        created_at = datetime.now()
        self.created_at = created_at
        self.updated_at = created_at
        # if given a dictionary **kwargs create instance with this instead
        if kwargs is not None and args is None:
            for key, value in kwargs.items():
                if key not in valid_attr:
                    pass
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, formatcode)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, formatcode)
        else:  # because nothing was created with kwargs call new() on storage
            storage.new(self)
        # otherwise create instance through assignment
        # id = str(uuid.uuid4())  # generates random UUID
        # self.id = id
        # created_at = datetime.now()
        # self.created_at = created_at
        # self.updated_at = created_at

    def __str__(self):
        """overwriting __str__ method to print object how we would like"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """update updated_at attr w/ current date time"""
        currentdt = datetime.now()
        self.updated_at = currentdt
        storage.save()  # call save(self) method on storage

    def to_dict(self):
        """create & return dictionary of instance attributes"""
        newdict = self.__dict__
        newdict['__class__'] = self.__class__.__name__
        newdict['updated_at'] = self.updated_at.isoformat()
        newdict['id'] = self.id
        newdict['created_at'] = self.created_at.isoformat()
        return newdict
