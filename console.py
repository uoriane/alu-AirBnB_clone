#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone project"""
    
    prompt = "(hbnb) "
    
    def __init__(self, stdin=None, stdout=None):
        super().__init__(stdin=stdin, stdout=stdout)
        self.classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        
        class_name = arg.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        
        print(all_objects[key])

    def do_destroy(self, arg):
        """Destroy an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances or instances of a specific class"""
        all_objects = storage.all()
        
        if not arg:
            print([str(obj) for obj in all_objects.values()])
            return
        
        class_name = arg.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        class_objects = [str(obj) for key, obj in all_objects.items() 
                        if key.startswith(f"{class_name}.")]
        print(class_objects)

    def do_update(self, arg):
        """Update an instance attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        if len(args) < 4:
            print("** value missing **")
            return
        
        attr_name = args[2]
        attr_value = args[3]
        
        # Remove quotes if present
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]
        
        # Cast attribute value to appropriate type
        instance = all_objects[key]
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            if attr_type == int:
                attr_value = int(attr_value)
            elif attr_type == float:
                attr_value = float(attr_value)
        
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
