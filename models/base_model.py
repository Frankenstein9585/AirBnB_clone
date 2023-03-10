import uuid
import datetime
import models

"""BaseModel Class"""


class BaseModel:
    """defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel object"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            # if kwargs.keys().__contains__('__class__'):
            kwargs.pop('__class__')
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.datetime.fromisoformat(v)
                setattr(self, k, v)

    def save(self):
        """updates the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        with 'created_at' and 'updated at' in ISO format
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__

    def __str__(self):
        """returns a string representation of a BaseModel object in dictionary form"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)
