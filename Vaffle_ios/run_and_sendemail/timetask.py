# -*- coding: utf-8 -*-
from tornado.ioloop import IOLoop
from apscheduler.schedulers.tornado import TornadoScheduler
from datetime import datetime
import time,sys,unittest
import os
import pymysql.cursors
sys.path.append("..//public")
from publicway import Publicway

sys.path.append('./UI')
sys.path.append('./DB')
sys.path.append('./testcase')
sys.path.append("./DATA")
sys.path.append('./img')


def heavengift():
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
    print(nowTime)
    sql = "select id from tbl_task_sync where project_id = 25 and status_ios=0 order by id desc limit 1"
    id = sql_hg_deploy(sql)
    # id = '%s' % id
    if id != "None":
        print ( "id：%s" % id )
        time.sleep(1)
        # status 状态0 改为 1: 执行过程中
        nowTime = int(time.time())
        sql1 = "update tbl_task_sync set status_ios = 1,updated_time='"+str(nowTime)+"' where id = "+str(id['id'])
        sql_hg_deploy(sql1)
        time.sleep(1)
        path=os.getcwd()
        print(os.getcwd())
        os.system("python3 "+path+"/run.py")
        time.sleep(1)
        # status 状态1 改为 2: 执行成功
        nowTime = int(time.time())
        sql3 = "update tbl_task_sync set status_ios = 2,updated_time='"+str(nowTime)+"' where id="+str(id['id'])
        sql_hg_deploy(sql3)

def sql_hg_deploy(s):
    # 连接MySQL数据库
    connection = pymysql.connect(host='172.100.10.10', port=3306, user='vf_auto', password='heavengifts.com',db='hg_deploy',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        # 通过cursor创建游标
    cursor = connection.cursor()

        # 创建sql 语句，并执行
    sql = s
    print("sql=",sql)
    execute=cursor.execute(sql)
    results=cursor.fetchall()
    for result in results:
        if result == None:
            return None
        else:
            return result
        # 提交SQL
    connection.commit()

if __name__ == '__main__':
    scheduler = TornadoScheduler()
    scheduler.add_job(heavengift, 'interval', seconds=60)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        pass
    # h=heavengift()
