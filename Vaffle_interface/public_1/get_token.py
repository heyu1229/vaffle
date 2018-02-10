# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,os
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
sys.path.append(os.getcwd())
from get_version import Version
from get_url import Url

#---------------获取token值----------------------
class Token():
    def __init__(self):
        #获取版本
        self.version =Version().test_version()
        self.base_url0 = Url().test_url()+'/token'
    '''
    def test_token(self,payload):

        headers = {'device': 'android ','version': self.version,'lang': 'en','timestamp': '1493780505','login':'none'}
        r = requests.post(self.base_url0,params=payload,headers=headers)
        content=r.json()
        print(content)
        self.token = content['token']
        return self.token
    '''
    def test_token1(self,payload,member_id):


        headers = {'device': 'android ','version': self.version,'lang': 'en','timestamp': '1493780505','login':member_id,"serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url0,params=payload,headers=headers)
        content=r.json()
        print(content)
        self.token = content['token']
        return self.token

