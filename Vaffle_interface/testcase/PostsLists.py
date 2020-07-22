import unittest
import requests
from public_1.get_token import Token
from public_1.get_url import Url
from public_1.get_version import Version


class PostsListsget_sign_in(unittest.TestCase):

    def setUp(self):
        url = Url ().test_url()
        self.base_url = url+'/posts/lists'
        self.version =Version().test_version()
    #用户已登录
    def testcase_001(self):
        #获取token
        payload = {"page":"1","type":"post"}
        list1 = ["page=1","type=post"]
        token, uuid, timeStamp = Token ().test_token ( list1 )

        headers = {"device": "android ", "version": "3.9.0", "lang": "en", "timestamp": timeStamp, "token":token,"uuid":uuid,
                   "serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        #print(result)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

    #用户未登录
    def testcase_002(self):
        #获取token
        payload = {"page":"1","type":"post"}
        list1 = ["page=1","type=post"]
        token,timeStamp = Token().test_token1( list1)
        headers = {"device": "android ", "version": self.version, "lang": "en", "timestamp": timeStamp, "token":token,
                   "serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main ()