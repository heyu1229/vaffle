# -*- coding: utf-8 -*-
from tornado.ioloop import IOLoop
from apscheduler.schedulers.tornado import TornadoScheduler
from datetime import datetime
import time,sys,unittest
import os
sys.path.append("..//public")
from punlicway import Publicway

sys.path.append('./UI')
sys.path.append('./DB')
sys.path.append('./testcase')
sys.path.append("./DATA")
sys.path.append('./img')


def heavengift():
    print('The time is: %s' % datetime.now())
    sql = "select id from task_sync where project_id = 25 and status=0 order by id desc limit 1"

    auto_type = '%s' % (sql)

    #是否执行下单(automatic_order:执行,automation:不执行)
    if auto_type =='automation' or auto_type =='automatic_order':

        print("add_order:%s"%auto_type)
        time.sleep(1)

        sql = SQL_HG().get_task_id()
        id = SQL_SEARCH_1().search(sql)
        id = '%s'%id
        print("id：%s"%id)
        time.sleep(1)

        # status 状态0 改为 1: 执行过程中
        sql2 = SQL_HG().update_task_execute()
        SQL_SEARCH_1().insert(sql2)
        time.sleep(1)
        os.system("python3 ./runtest.py")
        time.sleep(1)
        # status 状态1 改为 2: 执行成功
        sql3 = SQL_HG().update_task_finish()
        SQL_SEARCH_1().insert(sql3)
'''
def tick():
    print('Tick! The time is: %s' % datetime.now())
'''

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
