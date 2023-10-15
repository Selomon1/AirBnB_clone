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
from shlex import split
import cmd
import sys
import re


def parse(line):
    """ parses the command line arguments """
    handl_curl = re.search(r"\{(.*?)\}", line)
    handl_brkt = re.search(r"\[(.*?)\]", line)
    if handl_curl is None:
        if handl_brkt is None:
            return [i.strip(",") for i in split(line)]
        else:
            sp_line = split(line[:handl_brkt.span()[0]])
            splted1 = [i.strip(",") for i in sp_line]
            splted1.append(handl_brkt.group())
            return splted1
    else:
        sp_line = split(line[:handl_curl.span()[0]])
        splted1 = [i.strip(",") for i in sp_line]
        splted1.append(handl_curl.group())
        return splted1


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class interpreter
    Attributes:
            prompt (str): prompt command
            mods (list): list of class names
    """
    prompt = "(hbnb) "
    mods = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_EOF(self, line):
        """
        Signal to Exit the interpreter program
        """
        print()
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

    def do_quit(self, line):
        """
        Exit the command interpreter program
        """
        return True

    def help_quit(self):
        """
        Display quit command help information
        """
        print("Quit command to exit the program\n")

    def default(self, line):
        """ default response of cmd line """
        dict_args = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        comp = re.search(r"\.", line)
        if comp is not None:
            line1 = [line[:comp.span()[0]], line[comp.span()[1]:]]
            comp = re.search(r"\((.*?)\)", line1[1])
            if comp is not None:
                comm = [line1[1][:comp.span()[0]], comp.group()[1:-1]]
                if comm[0] in dict_args.keys():
                    kl = "{} {}".format(line1[0], comm[1])
                    return dict_args[comm[0]](kl)
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_create(self, line):
        """ create an instance of BaseModel """
        cmd_args = parse(line)
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        else:
            new_insta = eval(str(cmd_args[0]) + '()')
            print(new_insta.id)
            new_insta.save()

    def do_show(self, line):
        """ print the string representation of an instance """
        cmd_args = parse(line)
        stor = storage.all()
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(cmd_args[0], cmd_args[1]) not in stor:
            print("** no instance found **")
        else:
            print(stor["{}.{}".format(cmd_args[0], cmd_args[1])])

    def do_count(self, line):
        """ counts number of instances of class """
        cmd_args = parse(line)
        count = 0
        for obj in storage.all().values():
            if cmd_args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_destroy(self, line):
        """ deletes an instance based on the class name """
        cmd_args = parse(line)
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
        cmd_args = parse(line)
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
        cmd_args = parse(line)
        stor = storage.all()
        if len(cmd_args) == 0:
            print("** class name missing **")
            return False
        elif cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
            return False
        elif len(cmd_args) == 1:
            print("** instance id missing **")
            return False
        elif len(cmd_args) == 2:
            print("** attribute name missing **")
            return False
        elif len(cmd_args) == 3:
            try:
                type(eval(cmd_args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        elif len(cmd_args) == 4:
            obj = stor["{}.{}".format(cmd_args[0], cmd_args[1])]
            if cmd_args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[cmd_args[2]])
                obj.__dict__[cmd_args[2]] = valtype(cmd_args[3])
            else:
                obj.__dict__[cmd_args[2]] = cmd_args[3]
        elif type(eval(cmd_args[2])) == dict:
            obj = stor["{}.{}".format(cmd_args[0], cmd_args[1])]
            for k, v in eval(cmd_args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
