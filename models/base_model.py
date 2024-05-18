"""Module that defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defining all common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Datetime when the instance is created.
        updated_at (datetime): Datetime when the instance is last updated.
    """

    def __init__(self, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
            **kwargs: Keyword args for attribute values. If kwargs is empty,
                      new instance is created with unique id, created_at, and
                      updated_at. If kwargs is not empty, recreates an instance
                      from a dictionary representation.
        """
        if kwargs:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            kwargs.pop('__class__', None)
            for k, val in kwargs.items():
                if k in ('created_at', 'updated_at') and isinstance(val, str):
                    self.__dict__[k] = datetime.strptime(val, fmt)
                else:
                    self.__dict__[k] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Update the updated_at attribute with the current datetime and save the
        instance.
        """
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance.

        Returns:
            dict: Dictionary containing all keys/values of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        if isinstance(new_dict.get('created_at'), datetime):
            new_dict['created_at'] = new_dict['created_at'].isoformat()
        if isinstance(new_dict.get('updated_at'), datetime):
            new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
