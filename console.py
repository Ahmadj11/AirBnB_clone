#!/usr/bin/python3
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    'promt for the command line'
    prompt = '(hbnb)'
    file = None

def do_quit(self, q):
    "exit command"
    sys.exit()

def do_EOF(self, eof):
    "exit command"
    sys.exit()

def create(self, obj):
    "creates a new instance object"
    newmodel = BaseModel()

if __name__ == '__main__':
     HBNBCommand().cmdloop()

