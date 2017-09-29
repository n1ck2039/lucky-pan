import requests
import unittest
import json

target_url = "http://localhost:3000"


class TestMB(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_job(self):
        payload = {'type': 'classification', 'schedule': '300000', 'contentSourceId': 192728}
        r1 = requests.post(target_url + "/classify/v1/nicks_tenant/jobs", json=payload)
        self.assertEqual(r1.status_code, 200)
        response_body = json.loads(r1.text)
        self.assertEqual(response_body['jobType'], 'classification')
        self.assertEqual(response_body['priority'], 1)
        self.assertEqual(response_body['state'], 'running')

    def test_create_subjob(self):
        payload = {'job-id': 1234, 'type': 'classification', 'state': 'pending', 'priority': 1, 'schedule': 3000,
                   'description': 'primary job', 'tenant_id': 'nicks_tenant',
                   'request': {'contentSouceId': 122884296, "containerToFileCountList": [
                       {
                           "containerId": 4160,
                           "fileCount": 0
                       }
                   ]

                               }}

        r1 = requests.post(target_url + "/classify/v1/nicks_tenant/subjobs", json=payload)
        self.assertEqual(r1.status_code, 200)

    def test_update_job(self):
        payload = {"jobStatusRequest":"123"}
        r1 = requests.put(target_url + "/classify/v1/jobs/status", json=payload)
        self.assertEqual(r1.status_code, 204)


if __name__ == '__main__':
    unittest.main()