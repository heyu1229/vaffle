import unittest
import requests
class SignIn(unittest.TestCase):

    #def setUp(self):
        #self.r = FuncRequests()
        #self.base_url = 'https://apitest.vaffle.com/sign/in'

    def testcase_001(self):
        payload = {"account":"lisa","password":"111111"}
        self.base_url = 'https://apibeta.vaffle.com/sign/in'
        headers = {"device": "android ", "version": "3.8.6", "lang": "en", "timestamp": "1493780505", "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                   "login": "959","serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        print(result)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main ()