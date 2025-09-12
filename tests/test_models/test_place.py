#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """Unit tests for Place class"""

    def setUp(self):
        """Set up test objects"""
        self.place = Place()
        self.place.name = "My Place"
        self.place.city_id = "city123"
        self.place.user_id = "user123"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 100
        self.place.latitude = 1.234
        self.place.longitude = 5.678
        self.place.amenity_ids = []

    def tearDown(self):
        """Clean up"""
        del self.place

    def test_is_instance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes_exist(self):
        self.assertEqual(self.place.name, "My Place")
        self.assertEqual(self.place.city_id, "city123")
        self.assertEqual(self.place.user_id, "user123")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 1.234)
        self.assertEqual(self.place.longitude, 5.678)
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)

if __name__ == "__main__":
    unittest.main()

