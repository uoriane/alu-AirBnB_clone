#!/usr/bin/python3
"""
AirBnB Clone Project - Base Model
Core functionality for all model classes
"""
import uuid
import datetime


class BaseModel:
    """
    Base class providing common functionality for all model classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize instance with provided arguments or defaults"""
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                try:
                    if value.isdigit():
                        value = int(value)
                    elif value.replace('.', '', 1).isdigit():
                        value = float(value)
                except AttributeError:
                    pass
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            from models import storage
            storage.new(self)

    def save(self):
        """Update timestamp and persist to storage"""
        self.updated_at = datetime.datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Convert instance to dictionary representation"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """String representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)
