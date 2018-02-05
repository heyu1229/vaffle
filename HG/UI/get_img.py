# -*- coding:UTF-8 -*-
import unittest,os
import requests
import sys


#---------------获取img值----------------------
class Img():

    def test_errorimage(self):


        self.errorimage = 'E:\\python35\\HG\\heaven_formal\\img\\'
        # self.test_errorimage(os.getcwd()[:-9]+'\\img\\')

        return self.errorimage

    def test_success_image(self):


        self.success_image = 'E:\\python35\\HG\\heaven_formal\\img\\'
        # self.success_image = (os.getcwd()[:-9]+'\\img\\')

        return self.success_image