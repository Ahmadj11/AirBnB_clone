#!/usr/bin/python3
"""BaseModel class module that all AirBnB classes will inherit from"""


import json
import uuid


class BaseModel:
    """Defines all common attributes & methods for AirBnB classes"""
    def __init__(self, id, created_at, updated_at):
        self.id =  str(uuid.uuid4())