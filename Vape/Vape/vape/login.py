'''
@create : derrick
@Date :2019/9/19
@desc :
'''

from vape.request import vapePost, KEY


def signin(name, pwd, serial):
    params = {'account': name, 'password': pwd,
              'fcm_token': '770fec59ae4e074b0efed84089fb7711ac8db40f45887081b11d95f817a8afc9'}
    return vapePost('/sign/in', KEY, serial, params=params)