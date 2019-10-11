'''
@create : derrick
@Date :2019/9/19
@desc :
'''

import time
import hashlib
from datetime import datetime

p_device = "ios"
p_version = "3.7.3"
p_lang = "en"
p_company = "apple"
p_phone_model = "iPhone X"
p_system_version = "12.3.1"


def getToken(key, stamp, list=[]):
    list.sort()
    token = ''
    for pram in list:
        if token == '':
            token = pram
        else:
            token = token + '&' + pram
    hash_md5 = hashlib.md5()
    token = token + "&" + key + stamp
    hash_md5.update(token.encode(encoding='UTF-8'))
    md5_str = hash_md5.hexdigest()
    return md5_str.upper()


def getStamp():
    # 获取当前时间
    times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 转为时间数组
    timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    return str(int(time.mktime(timeArray)))


def getList(uuid, serial, stamp):
    param = ["device=" + p_device, "timestamp=" + stamp, "lang=" + p_lang, "version=" + p_version,
             "serial-number=" + serial, "company=" + p_company, "phone-model=" + p_phone_model,
             "system-version=" + p_system_version]
    if uuid == '' or uuid == 'none':
        return param
    else:
        param.append("uuid=" + uuid)
        return param


def getHeaders(uuid, screamer, stamp, token):
    header = dict()
    header['device'] = p_device
    header['timestamp'] = stamp
    header['lang'] = p_lang
    header['version'] = p_version
    header['serial-number'] = screamer
    header['company'] = p_company
    header['phone-model'] = p_phone_model
    header['system-version'] = p_system_version
    header['token'] = token
    header['User-Agent'] = 'python'
    header['content-type'] = 'application/x-www-form-urlencoded'
    if uuid != '' and uuid != 'none':
        header['uuid'] = uuid
        return header
    else:
        return header


if __name__ == '__main__':
    # print(Headers.getList('123','45','687','4353'))
    # print(Headers.token('luo','key','stamp',Headers.getList('luo','345345','687','4353')))
    # print(header.getStamp())
    # print(Headers.getHeaders('header'))
    # header.getHeaders('4063')
    print(getList('uuid', 'serial', 'stamp'))
    getHeaders('uuid', 'sernumber', 'stamp', 'token')
