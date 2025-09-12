#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class"""

    def setUp(self):
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        del self.storage
        del self.obj

    def test_all_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        self.storage.save()
        self.assertTrue(os.path.isfile(self.file_path))

    def test_reload_loads_file(self):
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertIn(key, new_storage.all())

if __name__ == "__main__":
    unittest.main()

