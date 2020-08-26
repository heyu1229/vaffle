# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,os


#---------------获取url值----------------------
class Url():

    def test_url(self):

        self.base_url = 'https://apitest.vaffle.com'
        #self.base_url = 'http://my.vaffle.com'

        return self.base_url

    def test_url1(self):

        self.base_url = 'https://apitest2.vaffle.com'
        #self.base_url = 'http://my.vaffle.com'

        return self.base_url

    def test_user(self):

        self.member_uuid = 'a5f10151-5685-4432-8c35-7198bc6511c9'

        return self.member_uuid

    #xls路径
    def test_path(self):

        # self.path = 'C:/Users/Administrator/PycharmProjects/vaffle_interface/test_code/Vaffle_interface/test_date/interface.xls'
        self.path = 'E:/python35/git/Vaffle/Vaffle_interface/test_date/interface.xls'
        # self.path = os.getcwd()[:-17]+'/test_date/interface.xls'
        # self.path = "/usr/lib/python3/heaven_interface_vaffle2.2/test_date/interface.xls"
        # self.path = 'E:/python35/HG/heaven_interface_vaffle2.0_auto2/test_date/interface.xls'
        return self.path

    # #服务器路径
    # def server_path(self):
    #
    #     self.path = '/usr/lib/python3/heaven_interface_vaffle2.0_auto2'
    #     return self.path
