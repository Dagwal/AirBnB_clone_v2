#!/usr/bin/python3

import cmd
import models
from shlex import split as split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

new_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'Amenity': Amenity, 'Place': Place, 'City': City,
               'Review': Review}


# Declare the HBNBCommand class
class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """
    prompt = '(hbnb) '

    def do_help(self, args):
        if args == "quit" or args == "EOF":
            print("Quit command to exit the program\n")
        elif args == "create":
            print("Create command to create new instance\n")
        elif args == "show":
            print("show an instance based on class name and id\n")
        elif args == "destroy":
            print("Delete command to delete an instance\n")
        elif args == "all":
            print("print all instances based or not class name\n")
        elif args == "update":
            print("update an instance base on class name and id\n")
        else:
            print("\nDocumented commands (type help <topic>):")
            print("=================================")
            print("EOF\tall\tcreate\tdestroy\thelp\tquit\tshow\tupdate")
# quit and EOF to exit the program

    def do_EOF(self, line):

        return True

    def do_quit(self, line):

        return True

    def emptyline(self):

        pass

    def ENTER(self):

        pass

    def do_create(self, line):

        splitline = split(line)
        if not splitline:
            print("** class name missing **")
        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")
        else:
            new_instance = new_classes[splitline[0]]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):

        if not line:
            print("** class name missing **")
        elif line.split()[0] not in new_classes.keys():
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            new_instance = "{}.{}".format(line.split()[0], line.split()[1])
            objs = models.storage.all()

            if new_instance not in objs:
                print("** no instance found **")
            else:
                print(objs[new_instance])

    def do_destroy(self, line):

        splitline = split(line)

        if not splitline:
            print("** class name missing **")
            return False

        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")

        elif len(splitline) < 2:
            print("** instance id missing **")

        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[new_instance]
                models.storage.save()

    def do_all(self, line):

        str_list = []

        if not line:
            for new_instance in models.storage.all().values():
                str_list.append(str(new_instance))
        else:
            splitline = split(line)
            if splitline[0] in new_classes:
                for key, value in models.storage.all().items():
                    if value.__class__.__name__ == splitline[0]:
                        str_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return False
        print(str_list)

    def do_update(self, line):

        splitline = split(line)

        if not splitline:
            print("** class name missing **")

        elif splitline[0] not in new_classes:
            print("** class doesn't exist **")

        elif len(splitline) < 2:
            print("** instance id missing **")

        elif len(splitline) < 3:
            print("** attribute name missing **")

        elif len(splitline) < 4:
            print("** value missing **")

        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[new_instance],
                        splitline[2], splitline[3])
                models.storage.save()

    def precmd(self, line):

        if not sys.stdin.isatty():
            print()
        if "." in line:
            line = line.replace(".", " ").replace("()", "")
            line = line.split(" ")
            line = f"{line[1]} {line[0]}"
            return cmd.Cmd.precmd(self, line)

        else:
            return cmd.Cmd.precmd(self, line)

    def do_count(self, line):

        count = 0
        for obj in models.storage.all().values():
            count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
