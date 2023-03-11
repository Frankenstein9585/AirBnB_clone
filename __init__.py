from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
obj_dict = storage.all()
id_list = list()
for v in obj_dict.values():
    id_list.append(v.to_dict()['id'])
