import cmd

"""This contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '

    # def do_help(self, arg: str):
    #     """Displays help for the various commands"""

    def emptyline(self) -> bool:
        """Prints new line when an empty line is passed to the interpreter"""
        ...

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
