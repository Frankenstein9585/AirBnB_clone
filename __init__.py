from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
obj_dict = storage.all()
obj_list = list()

for k in obj_dict.keys():
    obj_list.append(str(obj_dict[k]))



