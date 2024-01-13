#!/usr/bin/python3
# models/amenity.py
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity Instance """
        super().__init__(*args, **kwargs)
