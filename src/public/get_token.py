# -*- coding:UTF-8 -*-
import unittest
import requests
import sys


#---------------获取token值----------------------
class Token():

    def test_token(self,payload,url):

        self.base_url0 = url+'/token'

        headers = {'device': 'android ','version': '2.0.0','lang': 'en','timestamp': '1493780505','login':'none'}
        r = requests.post(self.base_url0,params=payload,headers=headers)
        content=r.json()
        self.token = content['token']
        return self.token

    def test_token1(self,payload,member_id,url):

        self.base_url0 = url+'/token'
        headers = {'device': 'android ','version': '2.0.0','lang': 'en','timestamp': '1493780505','login':member_id}
        r = requests.post(self.base_url0,params=payload,headers=headers)
        content=r.json()
        self.token = content['token']
        return self.token

    def test_token2(self,payload,member_id,url):

        self.base_url0 = url+'/token'
        headers = {'device': 'android ','version': '1.0.0','lang': 'en','timestamp': '1493780505','login':member_id}
        r = requests.post(self.base_url0,params=payload,headers=headers)
        content=r.json()
        self.token = content['token']
        return self.token
