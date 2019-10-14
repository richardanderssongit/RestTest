import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_something_a(self):

        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile/ri')
        if res.json()['lastName'] == 'Andersson':
            lastname = 'Ander'
        else:
            lastname = 'Andersson'

        res = requests.post('https://us-central1-mock-backend-60a04.cloudfunctions.net/setProfile/ri',
                            data={'firstName': 'Richie', 'lastName': lastname})
        self.assertEqual(requests.codes.ok, res.status_code)

        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile/ri')
        self.assertEqual(lastname, res.json()['lastName'])

    def test_another_b(self):
        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile')
        self.assertEqual(False, False)


if __name__ == '__main__':
    unittest.main()
