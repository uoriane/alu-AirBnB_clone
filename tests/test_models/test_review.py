#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """Unit tests for Review class"""

    def setUp(self):
        self.review = Review()
        self.review.text = "Great place!"
        self.review.user_id = "user123"
        self.review.place_id = "place123"

    def tearDown(self):
        del self.review

    def test_is_instance(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        self.assertEqual(self.review.text, "Great place!")
        self.assertEqual(self.review.user_id, "user123")
        self.assertEqual(self.review.place_id, "place123")

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("id", review_dict)

if __name__ == "__main__":
    unittest.main()

