#!/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
import requests
import sys
import json
import time,gc,xlrd

#---------------发布动态----------------------

class Publish(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://apitest2.vaffle.com/posts/publish'
        self.token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

    #-----------------发布图片动态----------------------------------
    def testcase_001(self):
        for i in range ( 0, 20 ):
            print("testcase_001发布图片动态：")
            obj = ({"path":"posts/1512710644871_767_android.jpg","ratio":1.23,"tag":1},)
            images = json.dumps(obj)
            print(images)
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            payload = {"content": "接口在"+date+"#SantaSide 测试发布图片","images": images,"category":"post"}
            headers = {"device": "android", "version": "4.1.2", "lang": "en", "timestamp":"1493780505", "token":self.token,"uuid":"a5f10151-5685-4432-8c35-7198bc6511c9",
                       "serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
            r = requests.post(self.base_url, params=payload, headers=headers)
            result = r.json()
            print(result)
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")