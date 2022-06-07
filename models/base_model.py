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
        # variable to help convert time str back to datetime object
        formatcode = "%Y-%m-%dT%H:%M:%S.%f"

        # if given dictionary **kwargs create instance it for deserialization
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        self.created_at = datetime.strptime(value, formatcode)
                    elif key == 'updated_at':
                        self.updated_at = datetime.strptime(value, formatcode)
                    else:  # account for all given attr in instances dictionary
                        setattr(self, key, value)
        else:  # no dictionary means this is your normal instantiation
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        newdict = {}  # insure we get a serializable object & protect og
        for element in self.__dict__:
            # copy __dict__ element by element
            newdict[element] = self.__dict__[element]
        # update newdict's elements accordingly w/o changing og
        newdict['__class__'] = self.__class__.__name__
        newdict['updated_at'] = self.updated_at.isoformat()
        newdict['created_at'] = self.created_at.isoformat()
        return newdict
