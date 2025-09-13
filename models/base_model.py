#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in the AirBnB clone project"""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Import storage here to avoid circular import
            from models import storage
            storage.new(self)

    def __str__(self):
        """Return string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with current datetime and save to storage"""
        self.updated_at = datetime.now()
        # Import storage here to avoid circular import
        from models import storage
        storage.save()

    def to_dict(self):
        """Return dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
