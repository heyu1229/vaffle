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

#---------------系统翻译【POST】---------------------
class discover_system_translate(unittest.TestCase):

    def setUp(self):
        url = Url ().test_url()
        self.base_url = url+'/system/translate'
        self.version =Version().test_version()
    #用户已登录
    def testcase_001(self):
        #获取token
        payload = {"targetLanguage": "ru","content": "你好，我是何钰"}
        headers = {"device": "android", "version": "4.0.4", "lang": "en", "timestamp": "1564033489234",
               "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
               "uuid": "b4156aea-a968-4722-a4fd-1123ded04736", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
               "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url, params=payload,headers=headers )
        result = result.json ()
        print ( result )



if __name__ == "__main__":
    unittest.main()