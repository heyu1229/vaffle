'''
@create : derrick
@file :redisPractice.py
@Date :2019/9/30
@desc :
'''
import redis


def redis_del():
    pool = redis.ConnectionPool(host='172.100.10.5', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    r.delete('dailyIpRegisterLimit:201910108fd9a49378315ec12c9ed27ed50b0ad3d48fc4e9')
    #print(r.get('dailyIpRegisterLimit:2019101086badcfa1abf6d406f245f4d4efe30941fdfa12c'))


class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='172.100.10.5', port=6379)  # 连接Redis
        self.channel = 'monitor'  # 定义名称

    def publish(self, msg):  # 定义发布方法
        self.__conn.publish(self.channel, msg)
        return True

    def subscribe(self):  # 定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
