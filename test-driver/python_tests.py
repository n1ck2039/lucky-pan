import requests
import unittest
import json

target_url = "http://petstore-service"


class TestMB(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_pet(self):
        r1 = requests.get(target_url + "/v1/pets/lucky")
        self.assertEqual(r1.status_code, 200)
        response_body = json.loads(r1.text)
        self.assertEqual(response_body['name'], 'Lucky')
        self.assertEqual(response_body['type'], 'Dog')
        self.assertEqual(response_body['breed'], 'mixed')

    
if __name__ == '__main__':
