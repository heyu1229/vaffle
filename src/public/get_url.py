# -*- coding:UTF-8 -*-
import unittest
import requests
import sys


#---------------获取url值----------------------
class Url():

    def test_url(self,type):
        
        self.beta_url = 'https://apibeta.vaffle.com'
        self.pre_url = 'https://apipre.vaffle.com';
        self.www_url = 'https://api.vaffle.com';
        if type=='beta':
            return self.beta_url
        elif type == 'pre':
            return self.pre_url
        elif type == 'www':
            return self.www_url;


    def test_path(self):

        #self.base_url = 'https://apibeta.ohmyvapor.com'
        self.path = 'C:/Users/Administrator/Desktop/HG/bheaven_interface_vaffle2.0_auto/heaven_interface_vaffle2.0_auto/test_date/interface.xls'


        return self.path