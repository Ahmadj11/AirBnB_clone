#!/usr/bin/python3
"""writes class FileStorage serializes/deserializes insts to/from JSON file"""


import json
# from models.base_model import BaseModel
import os.path


class FileStorage:
    """defines class that helps w/ deserialization/serialization of objects"""
    # declare private attributes
    __file_path = "file.json"  # value is a placeholder since path comes later
    __objects = {}  # an empty dictionary for now, future home of all object

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects  # instance methods instantiate class atrr onsite

    def new(self, obj):
        """adds obj to __objects with <obj class name>.id as key"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file __file_path"""
        # fix error that class is not serializable json object
        jobject = {}  # create empty dictionary to hold class dictionary
        for key in self.__objects.items():  # start iterating thru dict
            # need to make __objects serializable and turn values into dict
            jobject[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as jfile:
            json.dump(jobject, jfile)

    def reload(self):
        """deserializes JSON file to __objects if __file_path exists"""
        file_exists = os.path.exists(self.__file_path)
        if file_exists:  # check json file existence
            with open(self.__file_path, encoding="utf-8") as jfile:
                # opened file for reading not read it
                redfile = jfile.read()
                # load read json file into  __objects
                self.__objects = json.loads(redfile)
            # create dictionary within dictionary
            # for key, value in tempobjects.items():
               # self.__objects[key] = value.to_dict() 
        else:
            return

# importing at end of file prevent circular import error for partial initiali.
from models.base_model import BaseModel
    # coommenting out next 3 lines b/c not needed & return not correct
    # def __init__(self):
    # self.__objects = __objects
    # return __objects.__dict__

    # objects is private needs double under scores
    # def all(self):
    # return self.objects

# def new(self, obj):
# pass

# def save(self):
# pass

# def reload(self):
# pass
