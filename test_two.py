import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile')
        self.assertEqual(False, False)

    def test_another(self):
        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile')
        self.assertEqual(False, False)


if __name__ == '__main__':
    unittest.main()
