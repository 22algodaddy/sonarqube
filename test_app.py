# test_app.py
import unittest
from main import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), 'Hello, World!')
