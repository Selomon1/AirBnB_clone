#!/usr/bin/python3


from models import storage
from models.base_model import BaseModel
import cmd
import sys
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    mods = ["BaseModel"]

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("ctrl + d to exit the program")

    def emptyline(self):
        pass

    def postloop(self):
        print()

    def do_quit(self, line):
        sys.exit()

    def help_quit(self):
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
        l = len(cmd_args)
        if l > 0 and cmd_args[0] not in HBNBCommand.mods:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if l > 0 and cmd_args[0] == obj.__class__.__name__:
                    obj_op.append(obj.__str__())
                elif l == 0:
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
