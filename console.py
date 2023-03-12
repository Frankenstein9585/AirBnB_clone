import cmd
from models.base_model import BaseModel
from __init__ import storage, obj_dict

"""This contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb) '

    # def do_help(self, arg: str):
    #     """Displays help for the various commands"""

    def emptyline(self) -> bool:
        """Prints new line when an empty line is passed to the interpreter"""
        ...

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
         and prints the id"""
        if not arg:
            print('** class name missing **')
            return
        else:
            if arg != 'BaseModel':
                print("** class doesn't exist **")
                return
        new_model = BaseModel()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.split()
        e = IndexError
        try:
            if args[0] != 'BaseModel':
                print("** class name doesn't exist **")
                return
        except e:
            print('** class name missing **')
            return

        try:
            if f'BaseModel.{args[1]}' not in obj_dict.keys():
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return

        print(obj_dict[f'BaseModel.{args[1]}'])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        e = IndexError
        try:
            if args[0] != 'BaseModel':
                print("** class name doesn't exist **")
                return
        except e:
            print('** class name missing **')
            return

        try:
            if args[1] not in obj_dict.keys():
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return

        obj_dict.pop(f'BaseModel.{args[1]}')
        storage.save()

    def do_all(self, arg):
        """Prints the string representation of an instance
               based on the class name and id"""
        args = arg.split()
        e = IndexError
        obj_list = list()
        try:
            if args[0] != 'BaseModel':
                print("** class name doesn't exist **")
                return
        except e:
            print('** class name missing **')
            return

        for k in obj_dict.keys():
            obj_list.append(str(obj_dict[k]))

        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        e = IndexError

        try:
            if args[0] != 'BaseModel':
                print("** class name doesn't exist **")
                return
        except e:
            print('** class name missing **')
            return

        try:
            if args[1] not in obj_dict.keys():
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return
        try:
            ...
        except e:
            print('** attribute name missing **')
            return

        try:
            ...
        except e:
            print('** value missing **')



    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
