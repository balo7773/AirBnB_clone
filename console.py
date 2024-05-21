#!/usr/bin/python3
"""
This module defines the HBNBCommand class which serves
as the entry point of the command interpreter.  """


import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class that provides several commands to interact
    with the storage system.
    """
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """
        Handles the EOF command to exit the program.
        """
        print()
        return True

    def help_EOF(self):
        """
        Provides help information for the EOF command.
        """
        print("EOF command to exit the program")

    def do_quit(self, args):
        """
        Handles the quit command to exit the program.
        """
        sys.exit()
        return True

    def help_quit(self):
        """
        Provides help information for the quit command.

        """
        print("Quit command to exit the program.")

    def emptyline(self):
        """
        Overrides the default behavior for an empty line.
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel and saves it to the JSON file.
        Usage: create <class name>
        """
        if not args:
            print('** class name missing **')
            return
        args_line = args.split()
        class_name = args_line[0]
        if class_name not in FileStorage.definedclass:
            print('** class name doesn\'t exist **')
            return
        else:
            class_instance = FileStorage.definedclass[class_name]()
            class_instance.save()
            print(class_instance.id)

    def do_show(self, args):
        """
        Prints the string rep of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        if not args:
            print('** class name missing **')
            return
        args_line = args.split()
        class_name = args_line[0]
        if class_name not in FileStorage.definedclass:
            print('** class name doesn\'t exist **')
            return
        if len(args_line) < 2:
            print('** instance id missing **')
            return
        class_instance_id = args_line[1]
        key = f"{class_name}.{class_instance_id}"

        if key not in storage.all():
            print('** no instance found **')
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        if not args:
            print('** class name missing **')
            return
        args_line = args.split()
        class_name = args_line[0]
        if class_name not in FileStorage.definedclass:
            print('** class name doesn\'t exist **')
            return
        if len(args_line) < 2:
            print('** instance id missing **')
            return
        class_instance_id = args_line[1]
        key = f"{class_name}.{class_instance_id}"

        if key not in storage.all():
            print('** no instance found **')
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string rep of all instances based on the class name.
        Usage: all [<class name>]
        """
        class_instance = []
        args_line = args.split()
        if not args_line:
            print([str(value) for value in storage.all().values()])
            return
        class_name = args_line[0]

        if class_name not in FileStorage.definedclass:
            print('** class doesn\'t exist **')
        else:
            class_instance = [
                str(value) for value in storage.all().values()
                if value.__class__.__name__ == class_name
            ]
            print(class_instance)

    def do_update(self, args):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args_line = args.split()
        if len(args_line) < 1:
            print("** class name missing **")
            return
        if args_line[0] not in FileStorage.definedclass:
            print("** class doesn't exist **")
            return
        if len(args_line) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args_line[0], args_line[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args_line) < 3:
            print("** attribute name missing **")
            return
        if len(args_line) < 4:
            print("** value missing **")

        _key = args_line[2]
        _value = args_line[3]
        attr = None

        try:
            attr = eval(_value)
            setattr(storage.all()[key], _key, attr)
        except (SyntaxError, NameError):
            print("** value missing **")
        storage.save()
    
    def do_count(self, args):
        """Count the instance Created"""
        count = 0
        for key in storage.all():
            args_line = key.split(".")
            if args == args_line[0]:
                # if value["__class__"] == line:
                count += 1
        print(count)

    def handle_class_methods(self, *args):
        """Class Methods
        <cls>.all(), <cls>.show() etc
        """

        methods = ("all(", "show(", "count(", "create(")
        try:
            value = eval(arg)
            for i in methods:
                if i in args:
                    print(value)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except TypeError as b:
            field = b.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass
        
        def default(self, line: str) -> None:
        """Default Argument passed to the cmdline"""
        # splits the command line argument
        args = line.split(".")
        # Checks if the arg[0] is in the file storage and if args[1] ends with

        # all Available Instance
        class_names = ['User', 'BaseModel',
                       "Place", "City", "Amenity", "State",
                       "Review"
                       ]

        # prints all the instance based on the class name
        if args[0] in class_names and args[1].endswith("all()"):
            self.do_all(args[0])
        # counting the instance based on the class
        elif args[0] in class_names and args[1].endswith("count()"):
            self.do_count(args[0])
        elif args[0] in class_names and args[1].startswith("show"):
            # show a dictionary representation based on the id passed
            striped = args[1].strip("show(\"").strip("\")")
            key = "{}.{}".format(args[0], striped)
            if key not in storage.all():
                print('** no instance found **')
                return
            print(storage.all()[key])

        elif args[0] in class_names and args[1].startswith("destroy"):
            # delete an instance based on the id passed
            striped = args[1].strip("destroy(\"").strip("\")")
            key = "{}.{}".format(args[0], striped)
            if key not in storage.all():
                print('** no instance found **')
            del storage.all()[key]
            storage.save()

        elif args[0] in class_names and args[1].startswith("update"):
            striped = args[1].strip("update(\"").strip("\)")
            stripped_value = striped.split(",")

            # checks if it meets all expectations
            if len(stripped_value) < 3:
                print("** value missing **")
                return

            # stripped class_id, class_key, class_attr
            class_id = stripped_value[0].strip("\"")
            class_key = stripped_value[1]
            class_attr = stripped_value[2]

            key = "{}.{}".format(args[0], class_id)
            if key not in storage.all():
                print('** no instance found **')
                return

            attribute_value = None
            attr_key = None

            try:
                attribute_value = eval(class_attr)
                attr_key = eval(class_key)
                setattr(storage.all()[key], attr_key, attribute_value)
            except Exception as e:
                print("** value missing **")
            storage.save()
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
