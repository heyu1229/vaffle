# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc

from public_1.get_url import Url
from public_1.get_version import Version



#--------------投票---------------------
class posts_vote(unittest.TestCase):

    def setUp(self):
        #self.r = FuncRequests()
        self.path = Url().test_path()


    def testcase_001(self):

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/posts/vote'
        payload = {"post_id":"90003","optionIndex":"1"}
        headers = {"device": "android", "version": "4.0.0", "lang": "en", "timestamp": "1564033489234",
               "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
               "uuid": "a5f10151-5685-4432-8c35-7198bc6511c9", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
               "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url1, params=payload,headers=headers )
        result = result.json ()
        print ( result )




if __name__ == '__main__':
    unittest.main()