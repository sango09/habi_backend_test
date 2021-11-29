"""Test of the properties module."""
# Request
import requests

# Unit testing
import unittest


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8000'
        self.header = {'Content-Type': 'application/json'}

    def test_properties(self):
        """Test the properties module."""
        resp = requests.get(f'{self.url}/properties', headers=self.header)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.json())

    def test_validation_path(self):
        """Test the validation path."""
        resp = requests.get(f'{self.url}/properties/validation', headers=self.header)
        self.assertEqual(resp.status_code, 404)

    def test_validation_data(self):
        """Test the validation data."""
        resp = requests.get(f'{self.url}/properties', params={'city': 'bogota', 'status': 'pre_venta', 'year': 2021})
        self.assertEqual(resp.status_code, 200)
