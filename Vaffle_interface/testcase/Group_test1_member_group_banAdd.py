# -*- coding:UTF-8 -*-
import unittest
import requests
import time,gc

from public_1.get_url import Url
from public_1.get_version import Version



#---------------【群组】禁言、解禁接口----------------------
from public_1.sql_search import SQL_SEARCH_1
from public_1.sql_vaffle import SQL_vaffle


class Member_group_banadd(unittest.TestCase):

    def setUp(self):
        #self.r = FuncRequests()
        self.path = Url().test_path()

    #-----------------【群组】禁言、解禁接口---------------------------------
    def testcase_001(self):

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/member/group/banAdd'

        payload = {"type": "ban", "member_uuid": "06d3ae3c-e17c-48b8-90dd-7afcb97c734f", "ban_day": "30","guid": "d4f61542-fc1f-4155-aeec-a46d44e2955f"}
        headers = {"device": "android", "version": "3.8.3", "lang": "en", "timestamp": "1564033489234",
               "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
               "uuid": "b4156aea-a968-4722-a4fd-1123ded04736", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
               "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url1, params=payload,headers=headers )
        result = result.json ()
        print ( result )
    #-----------------【群组】解禁接口---------------------------------
    def testcase_002(self):

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/member/group/banAdd'
        payload = {"type": "unban", "member_uuid": "72e541fc-55d1-4d5d-809c-963c2255f050", "guid": "05965ae2-0979-41c1-be21-127aa5bd32cd"}
        headers = {"device": "android", "version": "3.8.3", "lang": "en", "timestamp": "1564033489234",
               "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
               "uuid": "e1399798-f1df-4f22-aea0-da0036ee03f1", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
               "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url1, params=payload,headers=headers )
        result = result.json ()
        print ( result )

    #-----------------【群组】禁言非小组成员---------------------------------
    def testcase_003(self):

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()
        self.base_url1 =url + '/member/group/banAdd'

        payload = {"type": "ban", "member_uuid": "84eff554-519f-4fc8-8904-8c4970046d8d", "ban_day": "1","guid": "d4f61542-fc1f-4155-aeec-a46d44e2955f"}
        headers = {"device": "android", "version": "3.8.3", "lang": "en", "timestamp": "1564033489234",
               "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
               "uuid": "44c20944-3bdd-4500-8784-0d198d8f66a0", "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
               "phone-model": "P10", "system-version": "8.0.0"}
        result = requests.post ( self.base_url1, params=payload,headers=headers )
        result = result.json ()
        print ( result )

    #-----------------批量给用户禁言----------------------------------
    def testcase_001(self):
        sheet_index = 1
        row = 11
        i = 38130
        print("testcase_001发布评论：")


        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.path = Url().test_path()
        self.version = Version().test_version()
        # 路径
        url = Url().test_url()


        while i <= 38180:
            #从数据库取UUID
            i = i+1
            sql = SQL_vaffle ().select_uuid (i)
            uuid = '%s' % SQL_SEARCH_1 ().search ( sql )
            self.base_url1 = url + '/group/addmember'
            payload = {"guid": "856dda7c-95e6-491b-bcc1-9d48d51ef00a", "type": "add"}
            headers = {"device": "android", "version": "3.8.3", "lang": "en", "timestamp": "1564033489234",
                       "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                       "uuid": uuid,
                       "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
                       "phone-model": "P10", "system-version": "8.0.0"}
            result = requests.post(self.base_url1, params=payload, headers=headers)
            result = result.json()
            print(result)
            self.base_url2 = url + '/member/group/banAdd'
            payload = {"type": "ban", "member_uuid": uuid, "ban_day": "30",
                       "guid": "856dda7c-95e6-491b-bcc1-9d48d51ef00a"}
            headers = {"device": "android", "version": "3.8.3", "lang": "en", "timestamp": "1564033489234",
                       "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                       "uuid": "a5f10151-5685-4432-8c35-7198bc6511c9",
                       "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
                       "phone-model": "P10", "system-version": "8.0.0"}
            result = requests.post(self.base_url2, params=payload, headers=headers)
            result = result.json()
            print(result)
        #global comment_id
        #comment_id = result["data"]["comment_id"]

        self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    unittest.main()