#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

"""The File Storage Class"""


class FileStorage:
    """This handles saving and loading from the JSON file"""
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Returns a dictionary representation of all objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Creates a new object"""

        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file"""

        path = FileStorage.__file_path

        obj_dict = {k: FileStorage.__objects[k].to_dict()
                    for k in FileStorage.__objects.keys()}

        with open(path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads the objects from JSON file"""

        path = FileStorage.__file_path

        try:
            with open(path) as file:
                obj_dict = json.load(file)
            for obj in obj_dict.values():
                class_name = obj['__class__']
                self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
