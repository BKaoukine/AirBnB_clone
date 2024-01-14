#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test if Amenity has the required attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_attribute_types(self):
        """Test if Amenity attributes have the correct types."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_str_representation(self):
        """Test the __str__ method of Amenity."""
        amenity = Amenity()
        expected_str = f"[<Amenity>] (<{amenity.id}>) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_str)


if __name__ == '__main__':
    unittest.main()
