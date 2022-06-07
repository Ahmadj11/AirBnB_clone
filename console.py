#!/usr/bin/python3
"""command interpreter to manage AirBnb objects"""

import cmd
# import sys


class HBNBCommand(cmd.Cmd):
    """defines command interpreter class"""
    # override default (cmd) prompt with following parent class attr
    prompt = '(hbnb)'
    # file = None

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

    # def create(self, args):
    # "creates a new instance object"
    # newmodel = BaseModel()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
