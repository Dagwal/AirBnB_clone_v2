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
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """ Exit the program."""
        print("")
        return True

    def emptyline(self):
        """ Shouldn’t execute anything. """
        pass

    def do_create(self, line):
        """Create command to create new User"""
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
        """Show command to show an instance based on class name and id"""
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
        """Delete command to delete an instance based on class name and id"""
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
        """All command to print all instances based or not class name"""
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
        """Update command to update an instance base on class name and id"""
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

    def default(self, line):
        """Parse and interpretates a line if not found on regular commands"""
        count = 0
        splitline = line.split('.', 1)
        if len(splitline) >= 2:
            line = splitline[1].split('(')
            """ Execute <class name>.all()"""
            if line[0] == 'all':
                self.do_all(splitline[0])
                """Execute <class name>.count() """
            elif line[0] == 'count':
                for key in models.storage.all():
                    if splitline[0] == key.split(".")[0]:
                        count += 1
                print(count)
                """Execute <class name>.show(<id>) """
            elif line[0] == 'show':
                id = line[1].split(')')
                str_id = str(splitline[0]) + " " + str(id[0])
                self.do_show(str_id)
                """Execute <class name>.destroy(<id>)"""
            elif line[0] == 'destroy':
                id = line[1].split(')')
                str_id = str(splitline[0]) + " " + str(id[0])
                self.do_destroy(str_id)
                """Execute <class name>.update(<id>"""
            elif line[0] == 'update':
                update = line[1].split(')')
                split = update[0].split('{')
                if len(split) == 1:
                    line = update[0].split(",")
                    str_id = str(splitline[0]) + " " + str(line[0]) + \
                        " " + str(line[1]) + " " + str(line[2])
                    self.do_update(str_id)
                else:
                    id = split[0][:-2]
                    str_dict = split[1][:-1]
                    delim = str_dict.split(',')
                    for row in delim:
                        key_value = row.split(':')
                        str_id = str(splitline[0]) + " " + str(id) + \
                            " " + str(key_value[0]) + " " + str(key_value[1])
                        self.do_update(str_id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
