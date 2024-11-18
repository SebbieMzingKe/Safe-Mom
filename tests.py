

import unittest
from app import app

app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'test_secret_key'

class TestApp(unittest.TestCase):
    # set up and tear down
    def set_up(self):
        self.app = app.test_client()
        self.app.testing = True

    def tear_down(self):
        pass

    # test home page
    def test_homepage_requires_login(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'login', response.location)