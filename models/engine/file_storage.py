import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = dict()

    def all(self) -> dict:
        return FileStorage.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        path = FileStorage.__file_path

        new_obj = {k: FileStorage.__objects[k].to_dict()
                   for k in FileStorage.__objects.keys()}

        with open(path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        path = FileStorage.__file_path

        try:
            with open(path) as file:
                object_json = json.load(file)
                for obj in object_json.values():
                    class_name = obj['__class__']
                    # obj.pop('__class__')
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
