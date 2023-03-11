from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

storage.reload()
obj_dict = storage.all()
id_list = []
id_ = 'b27f22a7-36a9-4912-bda0-c739609c93f9'

for v in obj_dict.values():
    # id_list.append(v.to_dict()['id'])
    if v.to_dict()['id'] == 'b27f22a7-36a9-4912-bda0-c739609c93f9':
        print(v)

if 'b27f22a7-36a9-4912-bda0-c739609c93f9' in id_list:
    ...

# print(obj_dict['BaseModel.b27f22a7-36a9-4912-bda0-c739609c93f9'])

 # def do_show(self, arg):
 #        """Prints the string representation of an instance
 #        based on the class name and id"""
 #        args = arg.split()
 #        e = IndexError
 #        id_list = list()
 #
 #        for v in models.obj_dict.values():
 #            id_list.append(v.to_dict()['id'])
 #
 #        try:
 #            if args[0] != 'BaseModel':
 #                print("** class name doesn't exist **")
 #                return
 #        except e:
 #            print('** class name missing **')
 #            return
 #        # storage.reload()
 #        # obj_dict = storage.all()
 #
 #        try:
 #            if args[1] not in id_list:
 #                print('** no instance found **')
 #                return
 #        except e:
 #            print('** instance id missing **')
 #            return
 #
 #        for v in models.obj_dict.values():
 #            if v.to_dict()['id'] == arg[1]:
 #                print(v)
