'''
@create : derrick
@file :signup.py
@Date :2019/10/10
@desc :
'''
import json

from vape.request import vapePost, KEY


def sign_up(email, nickname, serial):
    params = {'email': email, 'password': '111111', 'displayname': nickname, 'nickname': nickname,
              'equipment_number': '5299e97a-7057-34ee-9f60-85e358924ef3'}
    return vapePost('/sign/up', KEY, serial, params=params)


# sign = sign_up('52562f8523235@qq.com', 'derrokim2222', '788222521122')
# mix_secret = json.loads(sign)['data']['mix_secret']
# uuid = json.loads(sign)['data']['uuid']
# print(mix_secret)
# print(uuid)
