#basemodel class
import uuid
from datetime import datetime


class BaseModel:
    """"""
    def __init__(self, **kwargs):
       
        if kwargs == True:
            frmt = '%Y-%m-%dT%H:%M:%S.%f'
            del kwargs[__class__]
            for key, value in kwargs.items():
                self.__dict__[key] = value.datetime.strptime(kwargs[key], frmt)
        else:  
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        self.updated_at = datetime.utcnow()

        storage.new(self)
        storage.save()
        
        
        

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__

        if isinstance(new_dict.get('created_at'), datetime):
            new_dict['created_at'] = new_dict['created_at'].isoformat()
        if isinstance(new_dict.get('updated_at'), datetime):
            new_dict['updated_at'] = new_dict['updated_at'].isoformat()

        return new_dict