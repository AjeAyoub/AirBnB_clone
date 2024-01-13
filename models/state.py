#!/usr/bin/python3
# models/state.py
from models.base_model import BaseModel

class State(BaseModel):
    """State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State instance """
        super().__init__(*args, **kwargs)
