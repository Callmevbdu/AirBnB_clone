#!/usr/bin/python3
"""Represents the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The state ID.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
