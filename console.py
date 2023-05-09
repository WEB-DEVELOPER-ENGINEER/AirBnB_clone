#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
        quit and EOF to exit the program
        help
        a custom prompt: (hbnb)
    '''
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

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

    def do_create(self, line):
        '''
            Usage: create <class>
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.
        '''
        if not line:
            print("** class name missing **")
        else:
            try:
                cls = eval(line)
                print(eval(line)().id)
                storage.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''
            Usage: show <class> <id>
            Prints the string representation of an instance
            based on the class name and id.
        '''
        objdict = storage.all()
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        '''
            Usage: destroy <class> <id>
            Deletes an instance based on the class name and id.
        '''
        objdict = storage.all()
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        '''
            Usage: all or all <class>
            Prints all string representation of all instances
            based or not on the class name.
        '''
        arg = line.split()
        if len(arg) > 0 and arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            if len(arg) > 0:
                instances = [i.__str__() for i in storage.all().values()
                             if i.__class__.__name__ == arg[0]]
            else:
                instances = [i.__str__() for i in storage.all().values()]
            print(instances)

    def do_update(self, line):
        '''
            Usage: count <class>
            Updates an instance based on the class name and id by
            adding or updating attribute
        '''
        args = line.split()
        objdict = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
