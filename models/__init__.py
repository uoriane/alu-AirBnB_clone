#!/usr/bin/python3
"""
Models package initialization
Sets up storage instance and loads existing data
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()