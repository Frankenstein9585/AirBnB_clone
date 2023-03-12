from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

storage.reload()
obj_dict = storage.all()
print(obj_dict)
id_ = 'BaseModel.68707ec8-c64b-4f53-8819-25fb00210cf3'
print(obj_dict[id_])



