#!/usr/bin/python3

import json
from json.decoder import JSONDecodeError
from datetime import datetime



class FileStorage:
    """"""
    __file_path = "file.json"
    __objects = dict()
    
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        serialize = {
            key: value.to_dict()
            for key, value in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(serialize))
            
    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            deserialize = {}
            with open(FileStorage.__file_path, "r") as file:
                deserialize = json.loads(file.read())
            FileStorage.__objects = {
                key:
                    eval(obj["__class__"])(**obj)
                    for key, obj in deserialize.items()}
        except (FileNotFoundError, JSONDecodeError):
            pass