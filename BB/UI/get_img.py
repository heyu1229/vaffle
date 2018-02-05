# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,os

#---------------获取img值----------------------
class Img():

    def test_errorimage(self):


        self.errorimage = os.getcwd()+'\\img\\'

        return self.errorimage

    def test_success_image(self):


        self.success_image = os.getcwd()+'\\img\\'

        return self.success_image