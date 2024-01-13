#!/usr/bin/python3
"""Module for package initialization."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
