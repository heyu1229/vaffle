# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time,gc

from public_1.get_url import Url
from public_1.get_version import Version



#--------------发布Vote----------------------
class publish_vote(unittest.TestCase):

    def setUp(self):
        #self.r = FuncRequests()
        self.path = Url().test_path()


    def testcase_001(self):

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/posts/publish'
        obj = ({
    "viewPermission": 1,
    "votePermission": 1,
    "expireTimeStamp": 0,
    "expireTime": 3600,
   "totalVoteNum":4444,
    "options":[
        {
            "option":"选项一 译文",
            "optionSource":"选项一 原文",
            "num":0,
            "voteStatus":1
        },
        {
            "option":"选项二 译文",
            "optionSource":"选项二 原文",
            "num":0,
            "voteStatus":1
        }
    ]
})

        obj2 = ({"lat":12.343232,"lon":34.3232322})
        votes = json.dumps(obj)
        payload = {"content":"投票@queen","category":"vote","voteParams":votes,}
        headers = {"device": "android", "version": "4.0.0", "lang": "en", "timestamp": "1564033489234",
               "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
               "uuid": "a5f10151-5685-4432-8c35-7198bc6511c9", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
               "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url1, params=payload,headers=headers )
        result = result.json ()
        print ( result )


    def testcase_002(self):

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/posts/publish'
        obj = ({
    "viewPermission": 2,
    "votePermission": 2,
    "expireTimeStamp": 0,
    "expireTime": 3600,
   "totalVoteNum":4444,
    "options":[
        {
            "option":"选项一 译文",
            "optionSource":"选项一 原文",
            "num":0,
            "voteStatus":1
        },
        {
            "option":"选项二 译文",
            "optionSource":"选项二 原文",
            "num":0,
            "voteStatus":1
        }
    ]
})

        obj2 = ({"lat":12.343232,"lon":34.3232322})
        votes = json.dumps(obj)
        payload = {"content":"投票仅群组在成员看到","category":"vote","voteParams":votes,"guid":"dbceb048-6a97-47e9-bc99-d69153d28ca1"}
        headers = {"device": "android", "version": "4.0.0", "lang": "en", "timestamp": "1564033489234",
               "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
               "uuid": "a5f10151-5685-4432-8c35-7198bc6511c9", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
               "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url1, params=payload,headers=headers )
        result = result.json ()
        print ( result )


if __name__ == '__main__':
    unittest.main()