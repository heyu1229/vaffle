# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import json
import unittest
import requests
import time

from public.get_token import Token
from public.get_url import Url


class  SystemTestCase(unittest.TestCase):
    
    def setUp(self):

        #路径
        #self.url = Url().test_url('pre');
        self.url = Url().test_url('beta');
        self.member_id = '423'
    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_system(self):

        url1 = '/system/version'
        url1 = self.url +url1

        payload ={}
        token = Token ().test_token1 ( payload,self.member_id,self.url )
        start = time.time ()
        headers = {'device': 'android ', 'version': '2.0.0', 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        format_result=json.dumps(result,indent=1);
        print format_result;
            
        end = time.time ()
        
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except AssertionError as e:
            print("code返回值：非10000")

        try:
            self.assertEqual('', result['msg'])
            print("msg返回值：ok")
        except AssertionError as e:
            print("msg返回报错")
            
    def test_nation(self):
        url1 = '/system/nation'
        url1 = self.url +url1

        payload ={}
        token = Token ().test_token1 ( payload,self.member_id,self.url )
        start = time.time ()
        headers = {'device': 'android ', 'version': '2.0.0', 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        format_result=json.dumps(result,indent=1);
        print format_result;
            
        end = time.time ()
        
        try:
            self.assertEqual(10000, result['code'])
            print("code返回值：10000")
        except AssertionError as e:
            print("code返回值：非10000")

        try:
            self.assertEqual('', result['msg'])
            print("msg返回值：ok")
        except AssertionError as e:
            print("msg返回报错")
        

if __name__ == '__main__':
    unittest.main()

