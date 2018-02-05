import unittest,time,sys

from PIL import Image
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from testcase.models.function import Function

sys.path.append("../DATA")
from login import TestLogin
from get_url import Url
from get_img import Img



class Test_personaladdress():
    def setUp(self):
        time.sleep(2)


    def testpersonal_address(self,driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn):

        time.sleep(2)
        # 确定我已满18岁
        driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
        time.sleep(2)

        # -------用户登录------
        TestLogin().testlogin(driver,An,Bn)
        time.sleep(3)
        try:
            # -----------------------点个人中心------------------------------
            driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[1]").click()
            time.sleep(4)

            # ------------------------点AddressBook页面---------------------------
            driver.find_element_by_xpath("html/body/div[3]/div[2]/div[1]/div/dl[4]/dd[3]/a").click()
            time.sleep(4)
            # 检查AddressBook页面是否显示收货人heyu
            assert driver.find_element_by_xpath(
                "html/body/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/ul/li[1]").text == "he yu"
            print("显示收货人he yu")
            time.sleep(1)
            # 检查AddressBook页面是否显示Putuo District
            try:
                assert driver.find_element_by_xpath(
                    "html/body/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/ul/li[2]").text == "Putuo District"
                print("显示收货street:Putuo District")
            except AssertionError as e:
                print("不显示收货street:Putuo District")
            time.sleep(1)
            # 检查AddressBook页面是否显示shanghai, shanghai 226300
            try:
                assert driver.find_element_by_xpath(
                    "html/body/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/ul/li[3]").text == "shanghai, shanghai 226300"
                print("显示收货province:shanghai, shanghai 226300")
            except AssertionError as e:
                print("不显示收货street:shanghai, shanghai 226300")
            time.sleep(1)
            # 检查AddressBook页面是否显示United States
            try:
                assert driver.find_element_by_xpath(
                    "html/body/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/ul/li[4]").text == "United States"
                print("显示收货country:United States")
            except AssertionError as e:
                print("不显示收货country:United States")
            time.sleep(1)
            # 检查AddressBook页面是否显示18888052583
            try:
                assert driver.find_element_by_xpath(
                    "html/body/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/ul/li[5]").text == "18888052583"
                print("显示收货phone:18888052583")
            except AssertionError as e:
                print("不显示收货phone:18888052583")



        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(driver)
            raise


        time.sleep(3)