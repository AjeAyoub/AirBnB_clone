#!/usr/bin/python3
"""Module for HBNB command interpreter """
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class for AirBnB project """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit program """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program """
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
