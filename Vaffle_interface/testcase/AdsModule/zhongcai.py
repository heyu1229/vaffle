# -*- coding:UTF-8 -*-
import unittest,re
import sys,time,gc,xlrd,json

import requests
import paramiko

from Vaffle_interface.public_1.func_requests import FuncRequests

#---------------举报动态-仲裁----------------------
class PostsReport(unittest.TestCase):

    def setUp(self):
        self.r = FuncRequests()

    #-----------------举报动态----------------------------------
    def testcase_001(self):
        print("testcase_001举报动态：")

        #先将数据库中的仲裁官的活跃时间改成48小时之内
        t = int(time.time())
        s = 'update vape_last_active_record set updated_at='+str(t)+' where member_id in (70058,70059,70060,70061,70062,70063,70064,70065,70066,70067)'
        # s1 = 'update vape_last_active_record set updated_at=' + str(
        #     t) + ' where member_id in (28428,28429,28430,28431,28432,28433)'
        self.r.sql_vaffle(s)

        for n in range(0, 1):
            # 调用发布接口发送一条动态，获取post_id
            member_id1 = "9e20c7e8-c708-4581-abcc-8ace238e8829"
            member_id2 = ""

            obj = ({"path": "posts/1512710644871_767_android.jpg", "ratio": 1.23, "tag": 1},)
            images = json.dumps(obj)
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            payload1 = {"content": "4b 违规接口在" + date + "测试发布post用于举报", "images": images, "category": "post"}
            version = '4.1.4'
            base_url1 = 'https://apitest.vaffle.com/posts/publish'
            token = 'FkUw1pOFkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVg'

            headers1 = {"device": "android ", "version": version, "lang": "en", "timestamp": "1493780505",
                       "token": token,
                       "uuid": member_id1, "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
                       "phone-model": "P10", "system-version": "system_version"}
            r1 = requests.post(base_url1, params=payload1, headers=headers1)
            result1 = r1.json()
            print('发帖情况：',result1)
            post_id = result1["data"]["post_id"]

            #举报该post
            base_url = 'https://apitest.vaffle.com/posts/report'
            payload ={"post_id": post_id,"reason_id":"21","type":2}
            member_id = "c1fb0127-d086-41b0-95dc-c1f046f859fb"
            member_id3 = "2f903a5f-5571-4207-a0fa-f3cb989517e8"
            # member_id = "abaf75a6-904d-4bc9-a1ad-c45077e437d0"
            headers = {"device": "android ", "version": version, "lang": "en", "timestamp": "1493780505",
                       "token": token,
                       "uuid": member_id, "serial-number": "48525687125863258471123568955554", "company": "HUAWEI",
                       "phone-model": "P10", "system-version": "system_version"}
            r2=requests.post(base_url, params=payload, headers=headers)
            result = r2.json()

            self.assertEqual(10000, result["code"])
            print("举报接口code返回值：10000")
            print(date)
            cmd = 'php /wwwroot/test.vaffle.com/website/artisan command:Arbirate markReportLog'
            r = ssh(cmd)
            print('r=',r)

if __name__=="__main__":
    unittest.main()

def ssh(cmd):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='172.100.10.5', port=22, username='root', password='MGd1ev397nNC')

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    result = stdout.read().decode()

    # 关闭连接
    ssh.close()
    return result