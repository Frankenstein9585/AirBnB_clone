import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        path = FileStorage.__file_path

        obj_dict = {k: FileStorage.__objects[k].to_dict()
                    for k in FileStorage.__objects.keys()}

        with open(path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        path = FileStorage.__file_path

        try:
            with open(path) as file:
                obj_dict = json.load(file)
            for obj in obj_dict.values():
                class_name = obj['__class__']
                self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
