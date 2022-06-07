#!/usr/bin/python3
"""command interpreter to manage AirBnb objects"""

import cmd
# import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """defines command interpreter class"""
    # override default (cmd) prompt with following parent class attr
    prompt = '(hbnb)'

    # the only other parameter of cmd methods represents the args from cmdline
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True  # returning true will exit the ci

    def do_EOF(self, args):
        """Exit program with EOF input"""
        return True

    def emptyline(self):
        """empty line input executes nothing"""
        pass

    def do_create(self, args):
        """Create command to create new instance of existing class"""
        arglst = args.split()
        if len(arglst) == 0:
            print ("** class name missing **")
            return
        if arglst[0] != "BaseModel":
            print ("** class doesn't exist **")
            return
        else:
            newinst = BaseModel()
            newinst.save()
            print (newinst.id)
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
