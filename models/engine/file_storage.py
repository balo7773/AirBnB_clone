#!/usr/bin/python3

"""Module that defines the FileStorage class.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.
        definedclass (dict): Dictionary to map class names to classes.
    """
    __file_path = "file.json"
    __objects = {}
    definedclass = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'Place': Place,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objects, file)

    def reload(self):
        """
        Deserializes JSON file to __objects (if JSON file (__file_path) exists)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_file = file.read()
                if obj_file:
                    loaded_obj_file = json.loads(obj_file)
                    for value in loaded_obj_file.values():
                        class_name = value['__class__']
                        class_obj = FileStorage.definedclass[class_name]
                        self.new(class_obj(**value))
        except FileNotFoundError:
            pass
