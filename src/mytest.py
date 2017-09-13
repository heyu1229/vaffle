# -*- coding:UTF-8 -*-
import json
import unittest
import requests
import time

from public.get_token import Token
from public.get_url import Url

#---------------积分等级首页----------------------
class Membership(unittest.TestCase):

    def setUp(self):

        #路径
        #self.url = Url().test_url('pre');
        self.url = Url().test_url('beta');
        self.member_id = '423'
    #-----------------积分等级首页----------------------------------
    def testcase_001(self):
        
        url1 = '/membership'
        url1 = self.url +url1

        payload ={}
        token = Token ().test_token1 ( payload,self.member_id,self.url )
        start = time.time ()
        headers = {'device': 'android ', 'version': '2.0.0', 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        format_result=json.dumps(result,indent=1);
        #print format_resul           
        self.assertEqual(10000, result['code'])
            
    def test_description(self):
        url1 = '/rewards/description'
        url1 = self.url +url1

        payload ={}
        token = Token ().test_token1 ( payload,self.member_id,self.url )
        start = time.time ()
        headers = {'device': 'android ', 'version': '2.0.0', 'lang': 'en', 'timestamp': '1493780505', 'token':token,'login': self.member_id}
        r = requests.post ( url1,params=payload,headers=headers )
        result=r.json()
        format_result=json.dumps(result,indent=1);
        print format_result;
        self.assertEqual(10000, result['code'])

if __name__ == '__main__':
    unittest.main()