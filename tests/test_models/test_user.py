#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime

class TestUser(unittest.TestCase):
    """Unit tests for User class"""

    def setUp(self):
        """Set up test objects"""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.password = "1234"

    def tearDown(self):
        """Clean up"""
        del self.user

    def test_is_instance(self):
        """Test User is instance of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes_exist(self):
        """Test all attributes exist"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.password, "1234")

    def test_to_dict(self):
        """Test to_dict method"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertEqual(user_dict["email"], "test@example.com")

    def test_str(self):
        """Test __str__ method"""
        self.assertIn("[User]", str(self.user))
        self.assertIn(self.user.id, str(self.user))

if __name__ == "__main__":
    unittest.main()

