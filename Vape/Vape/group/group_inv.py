import json

from vape.request import vapePost, KEY
'''
@create : derrick
@Date :2019/9/19
@desc :
'''

def group_invite_list(uuid, key, serial):
    params = {'guid': '6cdd9060-2cd8-498e-99ea-b49864c9d893', 'page': '1', 'last_member_uuid': ''}
    vapePost('group/invite/list', key, serial, params=params, uuid=uuid)


def group_invite_search(uuid, key, serial):
    params = {'type': '', 'keywords': '', 'page': '', 'last_member_uuid': '', 'guid': ''}
    vapePost('group/invite/search', key, serial, params=params, uuid=uuid)


# guid	string	是		群组的guid
# member_uuid	string	是		被邀请人用户uuid

def group_invite(uuid, key, serial):
    params = {'guid': '6b86ab5b-d99c-4db2-a5bc-8a2eb8891a78', 'member_uuid': '03d68089-18f0-4b96-8aca-94b95cd915be'}
    vapePost('group/invite', key, serial, params=params, uuid=uuid)


if __name__ == '__main__':
    serial = '3e543ret453t4rt23'
    params = {'account': 'derrick', 'password': '111111',
              'fcm_token': '770fec59ae4e074b0efed84089fb7711ac8db40f45887081b11d95f817a8afc9'}
    sign = vapePost('sign/in', KEY, serial, params=params)
    mix_secret = json.loads(sign)['data']['mix_secret']
    uuid = json.loads(sign)['data']['uuid']
    group_invite(uuid, mix_secret, serial)
    group_invite_list(uuid, mix_secret, serial)
