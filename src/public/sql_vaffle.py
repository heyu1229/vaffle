import sys,time



class SQL_vaffle():
    #status 状态(0: 新建提交, 1: 执行过程中, 2: 执行成功, 3: 执行失败, 4: 删除)

    def update_vape_members(self):
        sql = "update vape_members set email = '427871220222211@vk' where id = 438"
        return sql
