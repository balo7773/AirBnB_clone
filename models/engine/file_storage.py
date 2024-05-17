import json

class FileStorage:
  __file_path = "file.json"
  __objects = dict()

  def all(self):
    return self.__objects

  def new(self, obj):
    self.__objects[obj.id] = obj

  def save(self):
    objects = {}
    for key, value in self.__objects.items():
      objects[key] = value.to_dict()

    with open(self.__file_path, 'w', encoding='utf-8') as file:
      json.dump(objects, file)


  def reload(self):
    try:
      if self.__file_path == True:
        with open(self.__file_path, "r") as f:
          self.__objects = json.load(f)
    except FileNotFoundError:
        pass