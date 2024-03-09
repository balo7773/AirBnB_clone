#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    def do_EOF(self, args):
        """"""
        return True

    def do_quit(self, args):
        """"""
        return True
    
    def Empty_line(self):
        """"""
        return
    def do_create(self, args):
        """"""
        n = len(args)
        if n == 0:
            print('** class name missing **')
            return
        if args is True:
            args_line = args.split()
            if len(args_line) == 1 and args in self.classes.keys():
                data = self.classes[args]()
                data.save()
                print(data.id)
            else:
                print("** class doesn't exist **")
    
    def do_show(self, args):
        n = len(args)
        if n == 0:
            print('** class name missing **')
            return
        args_line = args.split()
        if args_line[0] != self.classes:
            print("** class doesn't exist **")
            return
        elif len(args_line) > 1:
            key = args_line()[0] + '.' + args_line()[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')
        
    def do_destroy(self, args):
        """"""
        n = len(args)
        if n == 0:
            print("** class name missing **")
            return
        args_line = args.split()
        try:
            obj = eval(args_line[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args_line) == 1:
            print('** instance id missing **')
            return
        if len(args_line) > 1:
            key = args_line[0] + '.' + args_line[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

        def do_all(self, args):
            """"""
            obj_list = []

            if args:
                args = args.split(' ')[0]
                if args not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                    return
                for key, value in storage._FileStorage__objects.items():
                    if key.split('.')[0] == args:
                        obj_list.append(str(value))
            else:
                for key, value in storage._FileStorage__objects.items():
                    obj_list.append(str(value))
            
            print(obj_list)

            
        def do_update(self, args):
            """"""
            n = len(args)
            new_args = args.split()
            if not n:
                print("** class name missing **")
            elif n == 1:
                print("** instance id missing **")
            elif n == 2:
                print("** attribute name missing **")
            elif n == 3:
                print("** value missing **")
            else:
                try:
                    storage.update_one(*new_args[0:4])
                except  ModuleNotFoundError:
                    print("** class doesn't exist **")
                except NameError:
                    print("** no instance found **")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()