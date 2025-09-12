#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unit tests for Amenity class"""

    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "WiFi"

    def tearDown(self):
        del self.amenity

    def test_is_instance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attribute_name(self):
        self.assertEqual(self.amenity.name, "WiFi")

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("id", amenity_dict)

if __name__ == "__main__":
    unittest.main()

