import cmd
from models.base_model import BaseModel
from __init__ import obj_dict, id_list

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
            if args[1] not in id_list:
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return

        for v in obj_dict.values():
            if v.to_dict()['id'] == args[1]:
                print(v)

    def do_delete(self, arg):
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
            if args[1] not in id_list:
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return

        for v in obj_dict.values():
            if v.to_dict()['id'] == args[1]:
                obj_dict.pop()

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
