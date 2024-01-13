#!/usr/bin/python3
"""Module for the HBNB command interpreter."""
# console.py
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** {}".format(str(e)))

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            key = "{}.{}".format(args[0], args[1])
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            key = "{}.{}".format(args[0], args[1])
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        try:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on & class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[key]
            setattr(obj, args[2], args[3])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit & program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit & program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on Empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
