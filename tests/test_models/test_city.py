#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Unit tests for City class"""

    def setUp(self):
        self.city = City()
        self.city.name = "Kigali"
        self.city.state_id = "state123"

    def tearDown(self):
        del self.city

    def test_is_instance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        self.assertEqual(self.city.name, "Kigali")
        self.assertEqual(self.city.state_id, "state123")

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("id", city_dict)

if __name__ == "__main__":
    unittest.main()

