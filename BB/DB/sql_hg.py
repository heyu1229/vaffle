import sys,time
'''
project_id =3 HG正式环境   15 Buybest正式环境
数据库字段add_order  -> auto_type
'automation'=>'普通自动化','automatic_order'=>'自动下单',
'''


class SQL_HG():
    #status 状态(0: 新建提交, 1: 执行过程中, 2: 执行成功, 3: 执行失败, 4: 删除)
    def get_task_id(self):

        sql = "select id from task_sync where project_id = 15 and status=0 order by id desc limit 1"
        return  sql

    def get_task_add_order1(self):
        #status已被改为1
        sql = "select auto_type from task_sync where project_id = 15 and status=1 order by id desc limit 1"
        return  sql


    def update_task_execute(self):
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(nowTime)
        sql = "update task_sync set status = 1,updated_at='"+nowTime+"' where project_id = 15 and status=0 order by id desc limit 1"
        return sql

    def update_task_finish(self):
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = "update task_sync set status = 2,updated_at='"+nowTime+"' where project_id = 15 and status=1 order by id desc limit 1"
        return sql

    def update_task_fail(self):
        sql = "update task_sync set status = 3,updated_at= where project_id = 15 and status=1"

#SQL_TEST_1().sql_test()