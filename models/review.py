#!/usr/bin/python3
"""Review - A class representing a review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review - A class representing a review.

    Public instance attributes:
        - place_id (str): The ID of the place being reviewed.
        - user_id (str): The ID of the user who wrote the review.
        - text (str): The text content of the review.

    Example Usage:
        >>> review_instance = Review()
        >>> review_instance.place_id = "123"
        >>> review_instance.user_id = "456"
        >>> review_instance.text = "A great experience,
                highly recommended!"
        >>> review_instance.save()
    """

    place_id = ""
    user_id = ""
    text = ""
