# -*- coding:UTF-8 -*-
import unittest
import requests
import time
import hashlib


#---------------获取token值----------------------
from public_1.get_url import Url
from public_1.get_version import Version


class SignIn():
    def __init__(self):
        self.version =Version().test_version()
        self.base_url = Url().test_url()+'/sign/in'

        self.list = ['device=android ', 'version=3.7.2', 'lang=en', 'timestamp=1493780505',
               'serial-number=48525687125863258471123568955554', 'company=HUAWEI',
               'phone-model=P10', 'system-version=system_version']


    def test_sign_in(self,name,password):

        #登录之后拿mix_secret
        payload = {"account":name,"password":password}
        headers = {"device": "android", "version": self.version, "lang": "en", "timestamp": "1493780505", "token":"FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg","serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        print(result)
        mix_secret = result["data"]["mix_secret"]
        uuid = result["data"]["uuid"]
        return  mix_secret,uuid