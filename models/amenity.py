#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity - A class representing an amenity.

    Attributes:
        name (str): The name of the amenity.

    Inherits from:
        BaseModel: The base class for all models.
    """

    name = ""
