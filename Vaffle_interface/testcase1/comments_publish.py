'''
@create : lisa
@file :11.py
@Date :2019/9/19
@desc :

'''
import unittest
import requests
from public_1.get_token import Token
from public_1.get_url import Url
from public_1.get_version import Version

#---------------发布评论----------------------
class CommentsPublish(unittest.TestCase):

    def setUp(self):
        url = Url ().test_url()
        self.base_url = url+'/comments/publish'
        self.version =Version().test_version()
    #用户已登录
    def testcase_001(self):
        #获取token
        payload = {"content":"aaa","is_post":"N","post_id":"44337"}
        list1 = ["content=aaa","is_post=N","post_id=44337"]
        token,uuid,timeStamp = Token().test_token( list1)
        headers = {"device": "android", "version": self.version, "lang": "en", "timestamp":timeStamp, "token":token,"uuid":uuid,
                   "serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        print(result)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")



if __name__ == "__main__":
    unittest.main()