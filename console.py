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
        """Create a new instance of BaseModel save it & print & id."""
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
        """Deletes an instance based on the class name & id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            cls = eval(class_name)
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all Instances """
        args = arg.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        try:
            class_name = args[0]
            cls = eval(class_name)
            for obj in cls.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        except (KeyError, NameError):
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            cls = eval(class_name)
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = all_objs[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_update_dict(self, arg):
        """Updates an instance based on the class name & id with a dictionary."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            cls = eval(class_name)
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** dictionary missing **")
            return

        try:
            dictionary = eval(args[2])
            if type(dictionary) is not dict:
                raise ValueError
        except (ValueError, SyntaxError):
            print("** invalid dictionary **")
            return

        instance = all_objs[key]
        for k, v in dictionary.items():
            setattr(instance, k, v)
        instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            cls = eval(class_name)
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()

        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
