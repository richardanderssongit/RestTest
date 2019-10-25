import unittest
import requests


class MyTestCase(unittest.TestCase):

    profiledata = {"contactAddress":
                       {"postalCode":"21448",
                        "city":"Malmö",
                        "country":"Sweden",
                        "streetName":"Street"},
                   "email":"test@test.test",
                   "familyName":"Andersson",
                   "deliveryAddress":
                       {"postalCode":"21448",
                        "city":"Malmö",
                        "country":"Sweden",
                        "streetName":"Street"},
                   "phone":"1334421",
                   "firstName":"Rickie"}
    resetdata = {
        "firstName": "Test",
        "familyName": "Testsson",
        "email": "test@test.com",
        "phone": "0702286781",
        "locale": "sv",
        "contactAddress": {
            "streetName": "Test Street",
            "postalCode": "21447",
            "country": "Singapore",
            "city": "Test-city"
        },
        "deliveryAddress": {
            "streetName": "Testing Street",
            "postalCode": "31446",
            "country": "Sweden",
            "city": "City of Test"
        }
    }
    base_url = 'https://us-central1-mock-backend-60a04.cloudfunctions.net/'

    def test_get_profile(self):
        res = requests.get(self.base_url + 'ri')
        self.assertEqual(requests.codes.ok, res.status_code)

    def test_edit_profile(self):

        res = requests.get(self.base_url + 'getProfile/ri')
        self.assertEqual(requests.codes.ok, res.status_code)
        if res.json()['familyName'] == 'Andersson':
            lastname = 'Ander'
        else:
            lastname = 'Andersson'

        res = requests.post(self.base_url + 'setProfile/ri',
                            data={'firstName': 'Richie', 'familyName': lastname})
        self.assertEqual(requests.codes.ok, res.status_code)

        res = requests.get(self.base_url + 'getProfile/ri')
        self.assertEqual(lastname, res.json()['familyName'])

    def test_edit_profile_2(self):

        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile/ri')
        self.assertEqual(requests.codes.ok, res.status_code)
        old_profile = res.json()

        res = requests.post('https://us-central1-mock-backend-60a04.cloudfunctions.net/setProfile/ri',
                            data=self.profiledata)
        self.assertEqual(requests.codes.ok, res.status_code)

        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile/ri')
        self.assertEqual(requests.codes.ok, res.status_code)
        self.assertEqual(self.profiledata, res.json())

        res = requests.post('https://us-central1-mock-backend-60a04.cloudfunctions.net/setProfile/ri',
                            data=old_profile)
        self.assertEqual(requests.codes.ok, res.status_code)

        res = requests.get('https://us-central1-mock-backend-60a04.cloudfunctions.net/getProfile/ri')
        self.assertEqual(requests.codes.ok, res.status_code)

    def reset_profile(self):

        res = requests.delete(self.base_url + "deleteProfile/" + 'ri')
        self.assertEqual(requests.codes.ok, res.status_code)
        res = requests.post(self.base_url + "createProfile/" + 'ri', json=self.resetdata)
        self.assertEqual(requests.codes.ok, res.status_code)


if __name__ == '__main__':
    unittest.main()
