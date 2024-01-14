#!/usr/bin/python3
"""Place - A class representing a place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place - A class representing a place.

    Public instance attributes:
        - city_id (str): The ID of the city where the place is located.
        - user_id (str): The ID of the user who owns the place.
        - name (str): The name of the place.
        - description (str): A description of the place.
        - number_rooms (int): The number of rooms in the place.
        - number_bathrooms (int): The number of bathrooms in the place.
        - max_guest (int): The maximum number
                of guests the place can accommodate.
        - price_by_night (int): The price per night for staying at the place.
        - latitude (float): The latitude coordinate of the place.
        - longitude (float): The longitude coordinate of the place.
        - amenity_ids (list): A list of amenity IDs associated with the place.

    Example Usage:
        >>> place_instance = Place()
        >>> place_instance.city_id = "SF"
        >>> place_instance.user_id = "123"
        >>> place_instance.name = "Cozy Cottage"
        >>> place_instance.description = "A charming cottage
                in the heart of the city."
        >>> place_instance.number_rooms = 2
        >>> place_instance.number_bathrooms = 1
        >>> place_instance.max_guest = 4
        >>> place_instance.price_by_night = 100
        >>> place_instance.latitude = 37.7749
        >>> place_instance.longitude = -122.4194
        >>> place_instance.amenity_ids = ["wifi", "kitchen", "parking"]
        >>> place_instance.save()
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
