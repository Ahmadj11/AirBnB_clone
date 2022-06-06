#!/usr/bin/python3
"""writes class FileStorage serializes/deserializes insts to/from JSON file"""


import json


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
        self.__objects["obj.__class__.__name__.id"] = obj

    def save(self):
        """serializes __objects to JSON file __file_path"""
        # fix error that class is not serializable json object
        with open(self.__file_path, 'w', encoding="utf-8") as jfile:
            json.dump(self.__objects, jfile)

    def reload(self):
        """deserializes JSON file to __objects if __file_path exists"""
        try:  # check json file existence EAFP style bc LBYL gave error
            with open(self.__file_path, encoding="utf-8") as jfile:
                # opened file for reading not read it
                redfile = jfile.read()
                # load read json file into  __objects
                self.__objects = json.loads(redfile)
        except:
            pass

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
