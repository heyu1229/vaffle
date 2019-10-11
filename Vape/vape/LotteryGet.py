'''
@create : derrick
@file :LotteryGet.py
@Date :2019/10/10
@desc :
'''
import json
from redisdb.redisPractice import redis_del
from utils.RandomValue import RandomEmail, random_name
from vape.request import vapePost
from vape.signup import sign_up


def luck_get(inv_code, mix_s, user_uuid, serial_number):
    params = {'invitation_code': inv_code}
    return vapePost('/lottery/get', mix_s, serial_number, uuid=user_uuid, params=params)


if __name__ == '__main__':
    for n in range(1,31):
        print('n=',n)
        redis_del()
        serial = random_name()
        print(RandomEmail())
        print(random_name())
        sign = sign_up(RandomEmail(), random_name(), serial)
        print(json.loads(sign))
        mix_secret = json.loads(sign)['data']['mix_secret']
        uuid = json.loads(sign)['data']['uuid']
        invitation_code = 'c'
        print(luck_get(invitation_code, mix_secret, uuid,serial))
