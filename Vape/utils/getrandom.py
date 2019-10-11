import random
'''
@create : derrick
@Date :2019/9/19
@desc :
'''

def rand():
    return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 32))



if __name__ == '__main__':
    print(rand())
