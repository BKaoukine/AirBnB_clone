#!/usr/bin/python3
"""BaseModel - A base class for other models."""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel - A base class for other models.

    Public instance attributes:
        - id (str): A unique identifier assigned with
                    a UUID when an instance is created.
        - created_at (datetime): The datetime when an instance is created.
        - updated_at (datetime): The datetime when an instance is created
                                and updated every time the object is changed.

    Public instance methods:
        - __str__(self): Returns a string representation of the object.
        - save(self): Updates the 'updated_at' attribute
        with the current datetime.
        - to_dict(self): Returns a dictionary containing
                        all keys/values of the instance.

    Example Usage:
        >>> my_model = BaseModel()
        >>> print(my_model)
        [<BaseModel>] (<unique_id>) {'id': <unique_id>,
                'created_at': <datetime>, 'updated_at': <datetime>}
        >>> my_model.save()
        >>> print(my_model.to_dict())
        {'id': <unique_id>, 'created_at': <isoformatted_datetime>,
        'updated_at': <isoformatted_datetime>, '__class__': 'BaseModel'}

    Note: The 'isoformatted_datetime'
            in the example represents the datetime in ISO format.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        if kwargs:
            # If kwargs is not empty, set attributes based on the dictionary
            # Convert 'created_at' and 'updated_at'
            # from strings to datetime objects
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip __class__ attribute
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            # If kwargs is empty, create 'id'
            # and 'created_at' as done previously
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the object."""
        return f"[<{self.__class__.__name__}>] (<{self.id}>) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
