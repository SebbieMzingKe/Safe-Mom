

import unittest
from app import app

app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'test_secret_key'

class TestApp(unittest.TestCase):
    # set up and tear down
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    # test home page
    def test_homepage_requires_login(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.location)
    
    # test login
    def test_login_page_loads(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'login', response.data)

    def test_valid_login(self):
        response = self.app.post('/login', data = dict(
            email = 'test@example.com',
            password = 'password123'
        ), follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful.', response.data)

    
    def test_invalid_login(self):
        response = self.app.post('/login', data = dict(
            email = 'wrong@example.com',
            password = 'wrongpassword'

        ), follow_redirects = True)
        self.assertIn(b'Login Failed.', response.data)

if __name__ == '__main__':
    unittest.main()
    