#!/usr/bin/python3
"""User - A class representing a user."""
from models.base_model import BaseModel


class User(BaseModel):
    """User - A class representing a user.

    Public instance attributes:
        - email (str): The email of the user.
        - password (str): The password of the user.
        - first_name (str): The first name of the user.
        - last_name (str): The last name of the user.

    Example Usage:
        >>> user_instance = User()
        >>> user_instance.email = "user@example.com"
        >>> user_instance.password = "password123"
        >>> user_instance.first_name = "John"
        >>> user_instance.last_name = "Doe"
        >>> user_instance.save()
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
