import unittest,time


class Publicway(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

    def login_vaffle(self,user,password):
        self.driver.implicitly_wait(20)
        # self.driver.switch_to.alert
        try:
            if self.driver.find_element_by_xpath("//*[@text='Updates']").is_displayed():
                self.driver.find_element_by_xpath("//*[@text='Cancel']").click()
        except:
            print("no update")
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/bottom_menu_home").click()
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/bottom_menu_me").click()
        # e1=self.driver.find_element_by_id("com.heavengifts.vaffle:id/l_param1")
        # e1s=e1.find_elements_by_class_name("android.widget.RelativeLayout")
        # e1s[1].send_keys(user)
        e1 = self.driver.find_element_by_id("com.heavengifts.vaffle:id/l_param1")
        e1.find_element_by_id("com.heavengifts.vaffle:id/ed_content").send_keys(user)
        e2=self.driver.find_element_by_id("com.heavengifts.vaffle:id/l_param2")
        # e2s=e2.find_elements_by_class_name("android.widget.RelativeLayout")
        # e2s[1].send_keys(password)
        e2.find_element_by_id ( "com.heavengifts.vaffle:id/ed_content" ).send_keys ( password )
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/btn_login").click()

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


if __name__ == '__main__':
    unittest.main()
