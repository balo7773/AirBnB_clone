#basemodel class
import uuid
from datetime import datetime
from models import storage


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
        self.updated_at = datetime.utcnow()
        storage.save()
        
        

    def to_dict(self):
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['__created_at__'] = self.created_at.isoformat()
        new_dict['__updated_at__'] = self.updated_at.isoformat()
        return new_dict
