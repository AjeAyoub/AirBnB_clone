#!/usr/bin/python3
"""Module for FileStorage class."""
# models/engine/file_storage.py
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """File storage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns & dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to & JSON file (path: __file_path)."""
        save_dict = {}
        for key, obj in FileStorage.__objects.items():
            save_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(save_dict, f)

    def reload(self):
        """Deserializes & JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                load_dict = json.load(f)
            for key, obj_dict in load_dict.items():
                class_name, obj_id = key.split('.')
                cls = BaseModel
                if class_name in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                    cls = eval(class_name)
                obj = cls(**obj_dict)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
