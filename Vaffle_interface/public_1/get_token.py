# -*- coding:UTF-8 -*-
import unittest
import requests
import time
import hashlib


#---------------获取token值----------------------
from public_1.get_sign_in import SignIn
from public_1.get_version import Version


class Token():
    def __init__(self):
        self.version =Version().test_version()
        self.list = ['device=android', 'version=3.7.2', 'lang=en',
               'serial-number=48525687125863258471123568955554', 'company=HUAWEI',
               'phone-model=P10', 'system-version=system_version']

    #已登录用户获取token和uuid
    def test_token(self,x,list1=[]):
        if x:
            list1=x
        print("list1:" ,list1)

        mix_secret,uuid = SignIn ().test_sign_in("lisa","111111")
        #时间戳
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 转为时间数组
        timeArray = time.strptime ( now, "%Y-%m-%d %H:%M:%S" )
        #转为时间戳
        timeStamp = str (int( time.mktime ( timeArray ) ))
        print("时间戳：",timeStamp)

        self.list.append("uuid="+uuid)
        #self.list.append("mix_secret="+ mix_secret)
        self.list.append("timestamp="+ timeStamp)
        #list消息头和消息体拼接
        self.list = self.list+list1
        #list排序
        self.list.sort()
        print("排序后的list：",self.list)
        #list后加mix_secret和timeStamp值
        self.list.append(mix_secret+timeStamp)
        #self.list.append(timeStamp)
        i = 0
        for x in self.list:
            if i == 0:
                token = self.list[0]
                i = i+1
            else:
                token =  token +"&" + x
                i = i+1
        print(token)
        #md5加密生成token
        token = hashlib.md5(token.encode(encoding='UTF-8')).hexdigest()
        #token转大写
        token = token.upper()
        print("生成的token:",token)
        return token,uuid,timeStamp

    #未登录Android用户获取token
    def test_token1(self,x,list1=[]):
        if x:
            list1=x
        print("list1:" ,list1)
        #android
        mix_secret = "7xSI8jWf0719fa7c4c88aa0a682F30BF346A31Ff2c2f9cbcfdf286121f220cb"
        #ios
        mix_secret = "7xSI8jWf07c4c88aa0a68FkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgf2c2f9c"
        #时间戳
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 转为时间数组
        timeArray = time.strptime ( now, "%Y-%m-%d %H:%M:%S" )
        #转为时间戳
        timeStamp = str (int( time.mktime ( timeArray ) ))
        print("时间戳：",timeStamp)
        #list消息头和消息体拼接
        self.list = self.list+list1
        #list排序
        self.list.sort()
        print("排序后的list：",self.list)
        self.list.append(mix_secret+timeStamp)
        i = 0
        for x in self.list:
            if i == 0:
                token = self.list[0]
                i = i+1
            else:
                token =  token +"&" + x
                i = i+1
        #md5加密生成token
        print(token)
        token = hashlib.md5(token.encode(encoding='UTF-8')).hexdigest()
        token = token.upper()
        print("生成的token:",token)
        return token,timeStamp
