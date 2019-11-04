# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,time
import json,xlrd
# sys.path.append("/usr/lib/python3/heaven_interface_vaffle2.0_auto2/public")
import global_list
sys.path.append(global_list.path+"/public_1")
from get_url import Url
from get_version import Version
#from get_token import Token
from read_data import Read_ExcelData
from write_data import Write_ExcelData
sys.path.append(global_list.path+"/log")
from interface_log import interface_log
from func_requests import FuncRequests

#---------------发送邀请----------------------
class Group(unittest.TestCase):

    def setUp(self):
       self.r=FuncRequests()

    #-----------------发送邀请---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 9

        member_id = 'b7186ab3-6fa7-4589-a698-2c8c60f66f6c'
        print ("testcase_001 发送邀请:")
        member_uuid={"045c4627-5829-4b4c-9cad-e924f5b08cc1",
                     "cf93eb4b-0a0f-4501-b9a9-592d4767562f",
                     "7deddc51-16f0-4b31-8d73-fb6e54ebd2d9",
                     "8b95fb0c-b6c0-4061-8d2b-66fdc04b9a0b",
                     "4d5b33b9-944e-41ce-b2c0-3560b15bc0ce",
                     "fe34fe67-50ec-4afd-adda-95eee165fbf5",
                     "83baf928-dcd2-4ea7-a61f-9aed3529a5b2",
                     "44f1668a-138d-4ae6-a3da-cff5c4334baa",
                     "aeed1bed-ffec-4416-8fe8-2a6aa4e99bb9",
                     "42db67f1-f109-4945-95ed-32058a7f0c16",
                     "de3dd4c1-eda5-4505-848d-7cb0eee16eef"
                     }
        a=0
        start = time.time()
        for n in member_uuid:
            print("n=",n)
            payload={"guid":"300d579c-1c82-4519-bff7-f2900dc95a10","member_uuid":n}
            result=self.r.interface_requests_payload(member_id,sheet_index,row,payload)
            a=a+1
            print("a=",a)
        end = time.time()
        self.assertEqual(10000, result['code'])
        print("花费时间：",end-start)

if __name__ == "__main__":
    unittest.main()