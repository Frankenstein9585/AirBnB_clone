#!/usr/bin/python3
"""env not needed for this task"""
import cmd
import os
import shlex
import re

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from __init__ import storage, obj_dict

"""This contains the entry point of the command interpreter"""


def tokenize(arg: str) -> list:
    """ Splits a string into tokens delimited by space
    Args:
        arg (string): strings to be split
    Returns:
        list: list of strings
    """
    token = re.split(r"[ .(),]", arg)
    return token


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
        """Prints new line when an empty line is passed to the interpreter\n"""
        ...

    def default(self, arg):
        """Default method"""

        func_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update}

        tokens = tokenize(arg)
        for key in func_dict.keys():
            # checking for commands to call
            if key == tokens[1]:
                # for if args is parentheses eg("something")
                if tokens[2] != "" and len(tokens) < 6:
                    # print(tokens)
                    striped_arg = tokens[2].replace('"', '')
                    args = f"{tokens[0]} {striped_arg}"
                    return func_dict[tokens[1]](args)
                elif len(tokens) > 6:
                    # for update version 1
                    # print(tokens)
                    arg1 = tokens[2].replace('"', '')
                    arg2 = tokens[4].replace('"', '')
                    arg3 = tokens[6].replace('"', '')
                    args = f"{tokens[0]} {arg1} {arg2} {arg3}"
                    # print(args)
                    return func_dict[tokens[1]](args)

                else:
                    # print(tokens)
                    return func_dict[tokens[1]](tokens[0])

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id\n"""

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
        """Prints the string representation
        of an instance based on the class name and id\n"""

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
        """Deletes an instance based on checks around  the class name
        and id\n"""

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
        """Prints the string representation of all instances\n"""

        args = arg.split()
        e = IndexError
        obj_list = list()
        if not arg:
            for k in obj_dict.keys():
                obj_list.append(str(obj_dict[k]))

        elif args[0] not in HBNBCommand.CLASSES:
            print("** class name doesn't exist **")
            return
        else:
            for k, v in obj_dict.items():
                if args[0] in k:
                    obj_list.append(str(v))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute\n"""
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

    def do_clear(self, args: str) -> None:
        """Clear the screen"""
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def do_count(self, arg):
        """counts"""

        args = arg.split()
        # set counter
        count = 0
        # get all object keys
        for k in obj_dict.keys():
            if args[0] in k:
                count += 1
        print(count)

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
