import unittest,time
import pymysql.cursors
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC


class Publicway(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def login_VFamily(self,user,password):
        # self.driver.implicitly_wait(20)
        # 点菜单进入登录页面
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        # 输入用户名和密码
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField').send_keys(
            user)
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField').send_keys(
            password)

        # 点击登陆按钮
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Log In\"]").click()

    def publish_post(self,post_context):
        # 点击发布按钮
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'
            ).click()
        self.driver.find_element_by_ios_predicate('name=="0"').click()
        # 选择第一张照片
        self.driver.find_element_by_accessibility_id('next white').click()
        self.driver.find_element_by_accessibility_id('OK(white)').click()  # 编辑页面点击提交照片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_class_name('XCUIElementTypeTextView').send_keys(date+post_context)  # 输入文本
        self.driver.find_element_by_accessibility_id("ok(black)").click()  # 打勾
        self.driver.find_element_by_ios_predicate("name == ' - tab - 5 of 5'").click()
        time.sleep(10)
        self.driver.find_element_by_accessibility_id("Account").click()
        time.sleep(2)
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})
        return date

    def sign_up(self):
        date = int(time.time())
        print("当前时间：%s" % date)
        displayname = "test" + date
        email = "test" + date + "@163.com"
        password = "111111"
        print("displayname:%s" % displayname)
        print("email:%s" % email)
        print("password:%s" % password)
        # 点菜单进入登录页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()
        # 点右上角Sign Up按钮进入注册页面
        self.driver.find_element_by_accessibility_id(" Sign Up").click()
        # 输入name/e-mail/password
        # 输入name/e-mail/password
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]').send_keys(
            displayname)
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]').send_keys(
            email)
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField').send_keys(
            password)
        # 　收起键盘
        self.driver.find_element_by_accessibility_id(" Sign Up").click()
        self.driver.find_element_by_accessibility_id("Next").click()

        # 选择已经18岁
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="agreement"]').click()
        # self.driver.find_element_by_accessibility_id("agreement").click()
        # 进入注册2页面点Sign Up按钮  注册成功后进入首页
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=' Sign Up']").click()
        # 打开me页面
        self.driver.find_element_by_xpath(
            '//XCUIElementTypeApplication[@name="VFamily"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeOther[5]').click()

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

        # 向左滑

    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)

        # 向右滑

    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

        # 向上滑

    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.4)
        self.driver.swipe(x1, y1, x1, y2, t)

        # 向下滑

    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.7)
        self.driver.swipe(x1, y1, x1, y2, t)

    def sql_vaffle(self,s):
        # 连接MySQL数据库
        connection = pymysql.connect(host='172.100.200.62', port=3306, user='vaffle', password='Vaffle.123',
                                     db='vaffle',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


        # 通过cursor创建游标
        cursor = connection.cursor()

        # 创建sql 语句，并执行
        sql = s
        cursor.execute(sql)

        # 提交SQL
        connection.commit()

    def sql_vaffle_post(self,s):
        # 连接MySQL数据库
        connection = pymysql.connect(host='172.100.200.62', port=3306, user='vaffle', password='Vaffle.123',
                                     db='vaffle_post',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


        # 通过cursor创建游标
        cursor = connection.cursor()

        # 创建sql 语句，并执行
        sql = s
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
    unittest.main()
