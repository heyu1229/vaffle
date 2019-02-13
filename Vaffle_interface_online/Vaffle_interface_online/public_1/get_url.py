# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,os


#---------------获取url值----------------------
class Url():

    def test_url(self):

        self.base_url = 'https://api.vaffle.com'
        return self.base_url

    #xls路径
    def test_path(self):

        # self.path = '/usr/lib/python3/heaven_interface_vaffle2.0_auto2/test_date/interface.xls'
        self.path = os.getcwd()[:-9]+'/test_date/interface_online_vaffle.xls'
        # self.path = "/usr/lib/python3/heaven_interface_vaffle2.2/test_date/interface.xls"
        # self.path = 'E:/python35/HG/heaven_interface_vaffle2.0_auto2/test_date/interface.xls'
        return self.path

    # #服务器路径
    # def server_path(self):
    #
    #     self.path = '/usr/lib/python3/heaven_interface_vaffle2.0_auto2'
    #     return self.path
