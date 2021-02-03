import pymysql as mdb
import time

#测试环境数据库名称
DATABASE_NAME = 'vaffle'
#host = 'localhost' or '172.0.0.1'
HOST = '172.100.200.62'
#端口号
PORT = '3306'
#用户名称
USER_NAME = 'root'
#数据库密码
PASSWORD = 'heavengifts'
#数据库编码
CHAR_SET = '65001 (UTF-8)'

# #测试环境数据库名称
# DATABASE_NAME = 'vaffle'
# #host = 'localhost' or '172.0.0.1'
# HOST = '34.213.99.41'
# #端口号
# PORT = '3306'
# #用户名称
# USER_NAME = 'root'
# #数据库密码
# PASSWORD = 'heavengifts'
# #数据库编码
# CHAR_SET = '65001 (UTF-8)'

class SQL_SEARCH_1():

    def search(sql):
        # 查询
        con = mdb.connect(HOST, USER_NAME, PASSWORD, DATABASE_NAME);
        with con:
            # 仍然是，第一步要获取连接的cursor对象，用于执行查询
            cur = con.cursor()
            # 类似于其他语言的query函数，execute是python中的执行查询函数
            cur.execute(sql)
            # 使用 fetchone() 方法获取一条数据
            data = cur.fetchone ()
            return (data[0])

"""
            # 使用fetchall函数，将结果集（多维元组）存入rows里面
            rows = cur.fetchall()
            for row in rows:
                if row==None:
                    return None
                else:
                    print(row)
                    return row
                time.sleep(3)

"""


