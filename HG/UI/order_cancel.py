import unittest,time,sys
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common import alert
from selenium.webdriver.support.ui import Select
from testcase.models.function import Function

sys.path.append("../DATA")
from data_info import heaven_info

from login import TestLogin
from get_url import Url
from get_img import Img


class TestOrderCancel():
    def setUp(self):
        time.sleep(2)
    '''
    def tearDown(self):
        self.driver.quit()
    '''

    def testorder_cancel(self,driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn):
        try:
            # 确定我已满18岁
            #driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div/div[2]/a[2]").click()
            driver.find_element_by_xpath("html/body/div[9]/div/div/div/div/div/div[2]/button[2]").click()
            time.sleep(2)
            #--------------------用户登录--------------------------
            TestLogin().testlogin(driver,An,Bn)
            time.sleep(3)
            #----------------------首页-----------------------------
            # 搜索商品名称
            driver.find_element_by_id("kw").send_keys(Cn)
            time.sleep(3)
            #点search按钮
            driver.find_element_by_id("searchTextBtn").click()
            time.sleep(6)
            #点击商品
            driver.find_element_by_xpath("html/body/div[3]/div/main/section[1]/ul/li[1]/div").click()
            time.sleep(5)
            #---------------进入商品详情页--------------------------------
            #选择Color--blue
            driver.find_element_by_xpath ( "html/body/div[3]/div/main/section[1]/div[2]/form/div[1]/div[5]/dl/div[2]/dd/ul/li[1]" ).click ()
            time.sleep(1)
            #Quantity
            driver.find_element_by_name("quantity").clear()
            time.sleep(1)
            driver.find_element_by_name("quantity").send_keys(Dn)
            time.sleep(1)
            #点Add to Cart
            driver.find_element_by_xpath ("html/body/div[3]/div/main/section[1]/div[2]/form/div[2]/button[1]" ).click ()
            time.sleep(4)

            # 将页面滚动条拖到顶部
            js = "var q=document.body.scrollTop=0"
            driver.execute_script(js)
            time.sleep(2)
            #点shopping Cart
            driver.find_element_by_xpath("html/body/header/div/div[2]/div[3]/div[2]").click()
            time.sleep(4)
            #点proceed to checkout
            driver.find_element_by_id("checkoutBT").click()
            time.sleep(4)
            # driver.switch_to_alert().dismiss ()
            # time.sleep(30)
            #aa = driver.switch_to_alert ()
            #print("aa:%s"%aa)
            #aa.accept ()
            #确认地址
            driver.find_element_by_xpath("html/body/div[3]/dl[1]/dd/div[2]/form/div[8]/div/button").click()
            time.sleep(4)
            '''
            #选择物流
            select = Select(driver.find_element_by_id("shippingMethods"))
            select.select_by_visible_text(En)
            time.sleep(2)
            '''
            #选择物流
            driver.find_element_by_id("shippingMethods").find_elements_by_tag_name("option")[1].click()
            time.sleep(2)


            #选择支付方式--预存款
            select = Select(driver.find_element_by_name("paymentMethod"))
            select.select_by_visible_text(Fn)
            time.sleep(2)
            #留言
            driver.find_element_by_name("note").send_keys(Gn)
            time.sleep(2)

            #获得下单之前的购物车商品名称goods_name_pre、总价格price_pre及excel表的数量
            goods_name_pre = driver.find_element_by_xpath("html/body/div[3]/div[3]/div/table/tbody/tr/td[1]/p[1]/a").text
            print("下单之前的购物车商品名称:%s"%goods_name_pre)

            #总价格为隐藏元素，单独处理

            price_pre1 = driver.find_element_by_id ( "total" ).text
            price_pre1 = price_pre1.split ( ' ' )
            price_pre = float ( price_pre1[1] )
            print("下单之前的购物车商品总价格:%s"%price_pre)
            quantity_pre = driver.find_element_by_xpath("html/body/div[3]/div[3]/div/table/tbody/tr/td[4]").text
            quantity_pre = int(quantity_pre)
            print("下单之前的购物车商品总数量:%s"%quantity_pre)

            #提交订单
            driver.find_element_by_id("submitOrder").click()
            time.sleep(6)
            #获取订单(未支付)
            order_pre = driver.find_element_by_id("order_id").text
            print("下单未付款orderID:%s" % order_pre)


            #不支付直接点订单详情
            if Hn == 2:
                # 点击查看订单详情按钮
                driver.find_element_by_xpath("html/body/div[3]/div[3]/div/div[2]/p[4]/a[2]").click()
                time.sleep(5)

                # 将页面滚动条拖到底部
                js = "var q=document.body.scrollTop=100000"
                driver.execute_script(js)
                time.sleep(2)
                #订单详情页--点cancel按钮
                driver.find_element_by_id("orderDel").click()
                #driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/p[2]/a[3]").click()
                time.sleep(2)
                #弹出框--输入取消原因
                driver.find_element_by_id("order-cancel-reason").send_keys("取消订单测试")
                time.sleep(4)
                #点confirm按钮
                driver.find_element_by_xpath(".//*[@id='order-cancel']/form/div[2]/button[1]").click()
                time.sleep(5)
                # 将滚动条移动到页面的顶部
                js = "var q=document.body.scrollTop=0"
                driver.execute_script(js)
                time.sleep(2)
                #断言--订单状态 Order status=Cancelled
                order_status = driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div[2]/p/em[3]").text
                print("当前订单状态：%s"%order_status)
                time.sleep(1)
                assert"Cancelled" == order_status
                print("断言取消订单成功")
                time.sleep(5)


        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(driver)
            raise
