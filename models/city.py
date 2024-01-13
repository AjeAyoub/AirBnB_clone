#!/usr/bin/python3
# models/city.py
from models.base_model import BaseModel

class City(BaseModel):
    """City class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize City Instance """
        super().__init__(*args, **kwargs)
