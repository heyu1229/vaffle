'''
@create : lisa
@file :thread_sign_in.py
@Date :2020/9/8
@desc :

'''
# _*_ coding:utf-8 _*_
import threading
from time import sleep
import unittest
import requests
import time,gc,sys

#-----------------------用户登录接口---------------------------
from Vaffle_interface.public_1.func_requests import FuncRequests

#-----------------用邮箱登录成功--------------------------------
def sign_in_task1():
    member_uuid = 'none'
    requests = FuncRequests ()
    sheet_index =0
    row = 3
    for i in range(0,2):
        result = requests.interface_requests(member_uuid,sheet_index,row)
        # self.assertEqual(10000, result["code"])
        print("code返回值：10000")

if __name__ == '__main__':
    t1 = threading.Thread (target=sign_in_task1 )
    # t2 = threading.Thread ( target=task2, args=('zhang',) )
    t1.start ()
    t1.join()
    # t2.start ()