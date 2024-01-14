#!/usr/bin/python3
"""HBNBCommand - A command-line interpreter for HBNB project."""
import cmd
import models
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_home = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}

class HBNBCommand(cmd.Cmd):
    """HBNBCommand - A command-line interpreter for HBNB project.

    Public instance attributes:
        - prompt (str): The prompt displayed at the command line.

    Public instance methods:
        - do_EOF(self, line): Handles the EOF command.
        - do_quit(self, line): Handles the quit command.
        - emptyline(self): Handles an empty line.
        - do_create(self, line): Handles the create command.
        - do_show(self, line): Handles the show command.
        - do_destroy(self, line): Handles the destroy command.
        - do_all(self, line): Handles the all command.
        - do_update(self, line): Handles the update command.

    Example Usage:
        $ ./console.py
        (hbnb) create BaseModel
        (hbnb) show BaseModel 1234-1234-1234
        (hbnb) destroy BaseModel 1234-1234-1234
        (hbnb) all
        (hbnb) update BaseModel 1234-1234-1234 name "new_name"
    """

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """Handles the EOF command."""
        return True

    def do_quit(self, line):
        """Handles the quit command."""
        return True

    def emptyline(self):
        """Handles an empty line."""
        pass

    def do_create(self, line):
        """Handles the create command."""
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
        elif args[1].lower() != 'basemodel':
            print("** class doesn't exist **")
        else:
            new_instance = args[1].join(())
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Handles the show command."""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[1].lower() != 'basemodel':
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:

            instance = f"{args[0]}.{args[1]}"
            if instance not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[instance])

    def do_destroy(self, line):
        """Handles the destroy command."""
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
        elif args[1].lower() not in class_home:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:

            instance = f"{args[0]}.{args[1]}"
            if instance not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(instance)
                storage.save()

    def do_all(self, line):
        """Handles the all command."""
        obj_list = []

        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            args = line.split()
            if args[0] not in class_home:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == args[0]:
                        obj_list.append(str(value))
                    print(obj_list)

    def do_update(self, line):
        """Handles the update command."""
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in class_home:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            new_str = f"{args[0]}.{args[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], args[2], args[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
