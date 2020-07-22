import unittest,time
import requests
from public_1.get_token import Token
from public_1.get_url import Url
from public_1.get_version import Version

#---------------【群组】搜索群内成员----------------------
from public_1.sql_search import SQL_SEARCH_1
from public_1.sql_vaffle import SQL_vaffle


class GroupMemberlistSearch(unittest.TestCase):

    def setUp(self):
        url = Url ().test_url()
        self.base_url = url+'/group/memberlist/search'
        self.version =Version().test_version()
    #用户已登录
    def testcase_001(self):
        #获取token
        payload = {"guid":"24","search_name":"1","page":"1"}
        list1 = ["guid=24","search_name=1","page=1"]
        token,uuid,timeStamp = Token().test_token( list1)
        headers = {"device": "android", "version": self.version, "lang": "en", "timestamp":timeStamp, "token":token,"uuid":uuid,
                   "serial-number":"48525687125863258471123568955554","company":"HUAWEI","phone-model":"P10","system-version":"system_version"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        print(result)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")
    def testcase_002(self):
        i = 38300
        print("testcase_001发布评论：")


        # 调用发布接口发送一条动态，获取post_id
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        while i <= 38300:
            #从数据库取UUID
            i = i+1
            sql = SQL_vaffle ().select_uuid (i)
            uuid = '%s' % SQL_SEARCH_1 ().search ( sql )
        #获取token
        payload = {"guid":"2e6ec55e-f7b3-4c87-9e41-9e2a8019379e","search_name":"queen","page":"1"}
        headers = {"device": "android", "version": "3.8.0", "lang": "en", "timestamp": "1564033489234",
                   "token": "FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg",
                   "uuid": uuid, "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
                   "phone-model": "P10", "system-version": "8.0.0"}
        r = requests.post(self.base_url, params=payload, headers=headers)
        print(r)
        result = r.json()
        print(result)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")


if __name__ == "__main__":
    unittest.main()