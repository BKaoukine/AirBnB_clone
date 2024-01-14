#!/usr/bin/python3
"""City - A class representing a city."""
from models.base_model import BaseModel


class City(BaseModel):
    """City - A class representing a city.

    Public instance attributes:
        - state_id (str): The state ID to which the city belongs.
        - name (str): The name of the city.

    Example Usage:
        >>> city_instance = City()
        >>> city_instance.state_id = "CA"
        >>> city_instance.name = "San Francisco"
        >>> city_instance.save()
    """

    state_id = ""
    name = ""
