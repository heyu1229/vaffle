import pymysql as mdb
import time

#数据库名称
DATABASE_NAME = 'omv'
#host = 'localhost' or '172.0.0.1'
HOST = '54.68.118.91'
#端口号
PORT = '22'
#用户名称
USER_NAME = 'ohmyvapor'
#数据库密码
PASSWORD = 'p2BaPHB8isoTeZe6vw.rocMJi'
#数据库编码
CHAR_SET = '65001 (UTF-8)'

class SQL_SEARCH_1():

    def search(self,sql):
        # 查询
        con = mdb.connect(HOST, USER_NAME, PASSWORD, DATABASE_NAME);
        with con:
            # 仍然是，第一步要获取连接的cursor对象，用于执行查询
            cur = con.cursor()
            # 类似于其他语言的query函数，execute是python中的执行查询函数
            cur.execute(sql)
            # 使用fetchall函数，将结果集（多维元组）存入rows里面
            rows = cur.fetchall()
            for row in rows:
                if row==None:
                    return None
                else:
                    return row
                time.sleep(3)

    ##插入
    def insert(self,sql):
        con = mdb.connect(HOST, USER_NAME, PASSWORD, DATABASE_NAME);
        cur = con.cursor()
        sta = cur.execute(sql)
        if sta == None:
            print('insert Failed')
        else:
            print('insert Done')

        con.commit()
        cur.close()
        con.close()

