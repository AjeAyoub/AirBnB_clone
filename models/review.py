#!/usr/bin/python3
# models/review.py
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize Review Instance """
        super().__init__(*args, **kwargs)