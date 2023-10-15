#!/usr/bin/python3
"""
HBNB Command console module
"""

from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
import cmd
import shlex
import sys


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class interpreter
    Attributes:
            prompt (str): prompt command
            mods (list): list of class names
    """
    prompt = "(hbnb) "
    mods = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """
        Signal to Exit the interpreter program
        """
        return True

    def help_EOF(self):
        """
        Display help information of interpreter program
        """
        print("ctrl + d to exit the program")

    def emptyline(self):
        """
        Doing nothing when empty line is entered
        """
        pass

    def postloop(self):
        """
        Exits to be overridden by subclasses
        """
        print()

    def do_quit(self, line):
        """
        Exit the command interpreter program
        """
        sys.exit()

    def help_quit(self):
        """
        Display quit command help information
        """
        print("Quit command to exit the program\n")

    def do_create(self, line):
        """ create an instance of BaseModel """
        cmd_args = shlex.split(line)
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        else:
            new_insta = eval(str(cmd_args[0]) + '()')
            new_insta.save()
            print(new_insta.id)

    def do_show(self, line):
        """ print the string representation of an instance """
        cmd_args = shlex.split(line)
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        else:
            stor = storage.all()
            inst1 = str(cmd_args[0]) + "." + str(cmd_args[1])
            if inst1 in stor:
                print(stor[inst1])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ deletes an instance based on the class name """
        cmd_args = shlex.split(line)
        stor = storage.all()
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(cmd_args[0], cmd_args[1]) not in stor.keys():
            print("** no instance found **")
        else:
            del stor["{}.{}".format(cmd_args[0], cmd_args[1])]
            storage.save()

    def do_all(self, line):
        """ prints a string representation of all instances based or not
        on the class name
        """
        cmd_args = shlex.split(line)
        stor = storage.all()
        obj_op = []
        le = len(cmd_args)
        if le > 0 and cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if le > 0 and cmd_args[0] == obj.__class__.__name__:
                    obj_op.append(obj.__str__())
                elif le == 0:
                    obj_op.append(obj.__str__())
            print(obj_op)

    def do_update(self, line):
        """ updates an instance based on the class name and id """
        cmd_args = shlex.split(line)
        stor = storage.all()
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif len(cmd_args) == 2:
            print("** attribute name missing **")
        elif len(cmd_args) == 3:
            print("** value missing **")
        inst1 = cmd_args[0] + "." + cmd_args[1]
        stor = storage.all()
        try:
            inst_obj = stor[inst1]
        except KeyError:
            print("** no instance found **")
        try:
            try_typ = type(getattr(inst_obj, cmd_args[2]))
            cmd_args[3] = try_typ(cmd_args[3])
        except AttributeError:
            pass
        setattr(inst_obj, cmd_args[2], cmd_args[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
