from UI.get_img import Img
import unittest,time

#--------------------插入错误图片---------------------------------------
class Function(unittest.TestCase):

    def insert_img(self,driver):
        # 图片名称加个时间戳
        nowTime = time.strftime ( "%Y%m%d.%H.%M.%S" )
        test_errorimage = Img ().test_errorimage ()
        driver.get_screenshot_as_file ( test_errorimage + 'error_%s.jpg' % nowTime )
        time.sleep(2)