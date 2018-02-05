import time,sys,unittest

sys.path.append("../DB")
from sql_search import SQL_SEARCH_1
from sql_hg import SQL_HG

#---------------获取add_order值( 是否需要执行下单  0 不执行 1 执行  null无任务)----------------------
class get_AddOrder(unittest.TestCase):

    def setUp(self):
        time.sleep(2)

    def test_add_order(self):

        sql = SQL_HG().get_task_add_order()

        add_order = '%s'% SQL_SEARCH_1().search(sql)
        print(add_order)
        return add_order