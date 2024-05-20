#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True
    
    def do_EOF(self, line):
        """Another clean way to exit the interpreter\n"""
        return True
    

    def do_create(self, arg):
        """Create a new instance of BaseModek, save it, and print the id """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        # new_instance = storage.create(class_name)
        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)
        
    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")
            
    
    def do_all(self, arg):
        """Print all string representation of all instance"""
        arg = arg.strip()
        objs = []
        if arg:
            if arg not in storage.classes().keys():
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                class_name = key.split('.')[0]
                if class_name == arg:
                    objs.append(str(obj))
        else:
            for key, obj in storage.all().items():
                objs.append(str(obj))
        print(objs)
        
        
    def do_update(self, arg):
        """Update an instance based on the class"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3].strip('"')
        instance = storage.all()[key]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        setattr(instance, attribute_name, attribute_value)
        instance.save()
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

            
if __name__ == '__main__':
    HBNBCommand().cmdloop()







# #!/usr/bin/python3
# import cmd
# from models import storage
# from models.base_model import BaseModel

# class HBNBCommand(cmd.Cmd):
#     prompt = "(hbnb) "

#     def emptyline(self):
#         pass

#     def do_quit(self, line):
#         """Quit command to exit the program"""
#         return True

#     def do_EOF(self, line):
#         """Another clean way to exit the interpreter"""
#         return True

#     def do_create(self, arg):
#         """Create a new instance of BaseModel, save it, and print the id"""
#         if not arg:
#             print("** class name missing **")
#             return
#         class_name = arg.split()[0]
#         if class_name not in storage.classes():
#             print("** class doesn't exist **")
#             return
#         new_instance = storage.classes()[class_name]()
#         new_instance.save()
#         print(new_instance.id)

#     def do_show(self, arg):
#         """Print the string representation of an instance"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         class_name = args[0]
#         if class_name not in storage.classes():
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         instance_id = args[1]
#         key = f"{class_name}.{instance_id}"
#         if key in storage.all():
#             print(storage.all()[key])
#         else:
#             print("** no instance found **")

#     def do_all(self, arg):
#         """Print all string representation of all instances"""
#         arg = arg.strip()
#         print(f"do_all called with arg: '{arg}'")  # Debugging line
#         objs = []
#         if arg:
#             if arg not in storage.classes().keys():
#                 print("** class doesn't exist **")
#                 return
#             for key, obj in storage.all().items():
#                 class_name = key.split('.')[0]
#                 if class_name == arg:
#                     objs.append(str(obj))
#         else:
#             for key, obj in storage.all().items():
#                 objs.append(str(obj))
#         print(objs)

#     def do_update(self, arg):
#         """Update an instance based on the class"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         class_name = args[0]
#         if class_name not in storage.classes():
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         instance_id = args[1]
#         key = f"{class_name}.{instance_id}"
#         if key not in storage.all():
#             print("** no instance found **")
#             return
#         if len(args) < 3:
#             print("** attribute name missing **")
#             return
#         if len(args) < 4:
#             print("** value missing **")
#             return
#         attribute_name = args[2]
#         attribute_value = args[3].strip('"')
#         instance = storage.all()[key]
#         try:
#             attribute_value = eval(attribute_value)
#         except (NameError, SyntaxError):
#             pass
#         setattr(instance, attribute_name, attribute_value)
#         instance.save()

#     def do_destroy(self, arg):
#         """Deletes an instance based on the class name and id"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         class_name = args[0]
#         if class_name not in storage.classes():
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         instance_id = args[1]
#         key = f"{class_name}.{instance_id}"
#         if key in storage.all():
#             del storage.all()[key]
#             storage.save()
#             print(f"Instance {key} deleted")  # Debugging line
#         else:
#             print("** no instance found **")

# if __name__ == '__main__':
#     HBNBCommand().cmdloop()
