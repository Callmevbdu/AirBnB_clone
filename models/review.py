#!/usr/bin/python3
"""Defines the 'Review' class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str): The place ID.
        user_id (str): The user ID.
        text (str): The text review.
    """

    place_id = ""
    user_id = ""
    text = ""
