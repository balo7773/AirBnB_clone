#!/usr/bin/python3

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_EOF(self, args):
        """"""
        print()
        return True
    
    def help_EOF(self):
        print("Command to exit the program")

    def do_quit(self, args):
        """"""
        sys.exit
        return True
    
    def help_quit(self):
        """Help information for quit command."""
        print("Quit command to exit the program.")
    
    def Empty_line(self):
        """"""
        pass
    
    def do_create(self, args):
        """ creates new instance based on the class passed """

        if  not args:
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
        """"""
        if  not args:
            print('** class name missing **')
            return
        args_line = args.split()
        class_name = args[0]
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
    
        class_instance = []
        args_line = args.split()
        name_mthd = __class__.__name__
        if args_line == False:
            print([str(value) for value in storage.all().values()])
            return
        class_name = args_line[0]

        if class_name not in FileStorage.definedclass:
            print('** class doesn\'t exist **')
        else:
            name_mthd = '__class__.__name__'
            class_instance = [
                        str(value) for value in storage.all().values()
                        if eval(f"value.{name_mthd}") == class_name
            ]
            print(class_instance)
            
    def do_update(self, args):
            """"""
            n = len(args)
            args_line = args.split()
            if n < 1:
                print("** class name missing **")
                return
            if args_line[0] not in FileStorage.definedclass:
                print("** class doesn't exist **")
                return
            if n < 2:
                print("** instance id missing **")
                return
            
            key = "{}.{}".format(args_line[0], args_line[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            
            if n < 3:
                print("** attribute name missing **")
                return
            if n < 4:
                print("** value missing **")
            
            _key = args_line[2]
            _value = args_line[3]
            attr= None

            try:
                attr = eval(_value)
                setattr(storage.all()[key], _key, attr)
            except:
                print("** value missing **")
            storage.save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
