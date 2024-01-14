#!/usr/bin/python3
"""State - A class representing a state."""
from models.base_model import BaseModel


class State(BaseModel):
    """State - A class representing a state.

    Public instance attributes:
        - name (str): The name of the state.

    Example Usage:
        >>> state_instance = State()
        >>> state_instance.name = "California"
        >>> state_instance.save()
    """

    name = ""
