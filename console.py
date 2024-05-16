#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """A command to graciously exit the console\n"""
        return True
    
    def do_EOF(self, line):
        """Another clean way to exit the interpreter\n"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()