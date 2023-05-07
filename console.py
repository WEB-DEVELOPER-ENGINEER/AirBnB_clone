#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    '''
        quit and EOF to exit the program
        help
        a custom prompt: (hbnb)
    '''
    prompt = "(hbnb) "

    def emptyline(self):
        '''
            an empty line + ENTER shouldn’t execute anything
        '''
        pass

    def do_quit(self, line):
        '''
            exit the program
        '''
        return True

    def do_EOF(self, line):
        '''
            exit the program
        '''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
