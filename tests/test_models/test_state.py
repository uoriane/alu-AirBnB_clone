#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Unit tests for State class"""

    def setUp(self):
        self.state = State()
        self.state.name = "Rwanda"

    def tearDown(self):
        del self.state

    def test_is_instance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_attribute_name(self):
        self.assertEqual(self.state.name, "Rwanda")

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)

if __name__ == "__main__":
    unittest.main()

