import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from __init__ import storage, obj_dict

"""This contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb) '

    CLASSES = {"BaseModel",
               "User",
               "State",
               "City",
               "Place",
               "Amenity",
               "Review"}

    # def do_help(self, arg: str):
    #     """Displays help for the various commands"""

    def emptyline(self) -> bool:
        """Prints new line when an empty line is passed to the interpreter"""
        ...

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print('** class name missing **')
            return
        else:
            if arg not in HBNBCommand.CLASSES:
                print("** class doesn't exist **")
                return
        new_model = eval(arg)()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""

        args = arg.split()
        e = IndexError
        try:
            if args[0] not in HBNBCommand.CLASSES:
                print("** class name doesn't exist **")
                return
        except e:
            print('** class name missing **')
            return

        try:
            if f'{args[0]}.{args[1]}' not in obj_dict.keys():
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return

        print(obj_dict[f'{args[0]}.{args[1]}'])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        args = arg.split()
        e = IndexError
        try:
            if args[0] not in HBNBCommand.CLASSES:
                print("** class name doesn't exist **")
                return
        except e:
            print('** class name missing **')
            return

        try:
            if f'{args[0]}.{args[1]}' not in obj_dict.keys():
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return

        obj_dict.pop(f'{args[0]}.{args[1]}')
        storage.save()

    def do_all(self, arg):
        """Prints the string representation of an instance based on the class name and id"""

        args = arg.split()
        e = IndexError
        obj_list = list()
        try:
            if args[0] not in HBNBCommand.CLASSES:
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
        args = shlex.split(arg)
        e = IndexError

        try:
            if args[0] not in HBNBCommand.CLASSES:
                print("** class name doesn't exist **")
                return
        except e:
            print('** class name missing **')
            return

        try:
            if f'{args[0]}.{args[1]}' not in obj_dict.keys():
                print('** no instance found **')
                return
        except e:
            print('** instance id missing **')
            return
        try:
            args[2]
        except e:
            print('** attribute name missing **')
            return

        try:
            args[3]
        except e:
            print('** value missing **')
            return

        obj = obj_dict[f'{args[0]}.{args[1]}']
        if args[2] in obj.__class__.__dict__.keys():
            # get the type of the current attribute value
            attr_type = type(obj.__class__.__dict__[args[2]])
            # cast the provided argument to the required type
            obj.__dict__[args[2]] = attr_type(args[3])
        else:
            obj.__dict__[args[2]] = args[3]

        storage.save()

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
