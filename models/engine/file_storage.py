import json
from models.base_model import BaseModel

class FileStorage:
  __file_path = "file.json"
  __objects = dict()
  
  definedclass = {
          'BaseModel': BaseModel,
  }

  def all(self):
    return self.__objects

  def new(self, obj):
    key = f"{obj.__class__.__name__}.{obj.id}"
    self.__objects[key] = obj


  def save(self):
    objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
    with open(self.__file_path, 'w', encoding='utf-8') as file:
        json.dump(objects, file)

  def reload(self):
    try:
        with open(self.__file_path, 'r') as file:
            obj_file = file.read()
            if obj_file:
                loaded_obj_file = json.loads(obj_file)
                for value in loaded_obj_file.values():
                    class_name = value['__class__']
                    class_obj = FileStorage.definedclass[class_name]
                    self.new(class_obj(**value))
    except FileNotFoundError:
        pass
