import cmd

"""This contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Hii"""
    prompt = '(hbnb) '

    # def do_help(self, arg: str):
    #     """Displays help for the various commands"""

    def do_quit(self):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
