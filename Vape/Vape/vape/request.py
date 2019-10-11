'''
@create : derrick
@Date :2019/9/19
@desc :
'''
from os import environ
import json

from requests import post

from utils.headers import getStamp, getList, getHeaders, getToken

HTTP_BASE = environ.get('HTTPBIN_URL', 'https://apitest.vaffle.com')
KEY = '7xSI8jWf07c4c88aa0a68FkUw1pOBHh7xSI8jWf0X6JuryjWHjhuMapX69FKZSVgf2c2f9c'


def base(*suffix):
    return HTTP_BASE + '/'.join(suffix)


def postRequest(url, params, header):
    try:
        if params is not None and params != 'none':
            return post(base(url), data=params, headers=header).text
        else:
            return post(base(url), headers=header).text
    except Exception as err:
        print
        err


def dicttolist(mapping, lisr=[]):
    list_keys = list(mapping.keys())
    list_values = list(mapping.values())
    for index in range(len(list_keys)):
        lisr.append((list_keys[index]) + '=' + (list_values[index]))
    return lisr


def vapePost(url, secret, serial, **kwargs):  # params, uuid
    param = []
    stamp = getStamp()
    uuid = ''
    params = {}
    if 'uuid' in kwargs:
        uuid = kwargs['uuid']
    else:
        uuid = 'none'
    if 'params' in kwargs:
        params = kwargs['params']
        param = getList(uuid, serial, stamp)
        dicttolist(params, param)
    else:
        params = 'none'

    token = getToken(secret, stamp, param)
    header = getHeaders(uuid, serial, stamp, token)
    return postRequest(url, params, header)


if __name__ == '__main__':
    serial = '3e543ret453t4rt'
    params = {'account': 'derrick', 'password': '111111',
              'fcm_token': '770fec59ae4e074b0efed84089fb7711ac8db40f45887081b11d95f817a8afc9'}
    sign = vapePost('/sign/in', KEY, serial, params=params)
    mix_secret = json.loads(sign)['data']['mix_secret']
    uuid = json.loads(sign)['data']['uuid']
    p = {"post_id": "1119048", "praise_state": "1"}
    print(vapePost('/posts/praise', mix_secret, serial, params=p, uuid=uuid))
