import unittest,time,sys

from PIL import Image
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from testcase.models.function import Function

sys.path.append("../DATA")
from data_info import heaven_info

from login import TestLogin
from get_url import Url
from get_img import Img



class Testpurchase():
    def setUp(self):
        time.sleep(2)


    def testpurchase(self,driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn):
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
            #选择color--blue
            # select = Select(driver.find_element_by_name("productId"))
            # select.select_by_visible_text("Blue")
            driver.find_element_by_xpath ( "html/body/div[3]/div/main/section[1]/div[2]/form/div[1]/div[5]/dl/div[2]/dd/ul/li[1]" ).click ()
            time.sleep(1)
            #Quantity
            driver.find_element_by_name("quantity").clear()
            time.sleep(1)
            driver.find_element_by_name("quantity").send_keys(Dn)
            time.sleep(1)
            #点Add to Cart
            driver.find_element_by_xpath("html/body/div[3]/div/main/section[1]/div[2]/form/div[2]/button[1]").click()
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
            time.sleep(2)
            # driver.switch_to_alert ().dismiss ()
            # time.sleep(30)
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
            # price_pre1 = driver.find_element_by_id("order_total_amount").get_attribute("value")
            # price_pre = float(price_pre1)
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
            #断言订单提交成功
            ordersucess = driver.find_element_by_xpath ( "html/body/div[3]/div[3]/div/div[2]/h3" ).text
            # print(ordersucess)
            time.sleep ( 3 )
            assert 'Order Submitted!' == ordersucess
            print ( "断言订单支付成功" )

            if Hn == 1:
                #pay now
                driver.find_element_by_id("dopay").click()
                time.sleep(5)

                # 断言支付成功
                paysucess = driver.find_element_by_xpath ( "html/body/div[3]/div[2]/div/div[2]/h3" ).text
                # print(ordersucess)
                time.sleep ( 3 )
                assert 'Order paid Submitted!' == paysucess
                print ( "断言订单支付成功" )
                #点击查看订单详情按钮
                driver.find_element_by_xpath("html/body/div[3]/div[3]/div/div[2]/p[4]/a[2]").click()
                time.sleep(5)
            else:
                #点击查看订单详情按钮
                driver.find_element_by_xpath("html/body/div[3]/div[3]/div/div[2]/p[4]/a[2]").click()
                time.sleep(5)

            #-----------------------进入订单详情页-------------------------------
            #获得订单后的商品名称\价格、数量及订单号
            goods_name_after = driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div[5]/table/tbody/tr/td[1]/p[1]/a").text
            print("下单后订单详情页显示商品名称：%s"%goods_name_after)
            time.sleep(1)
            price_after1 = driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div[2]/p/em[1]").text
            price_after1 = price_after1.split(' ')
            price_after = float(price_after1[1])
            print("下单后订单详情页显示总价格：%s"%price_after)
            time.sleep(1)
            quantity_after = driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/div[5]/table/tbody/tr/td[2]").text
            quantity_after = int(quantity_after)
            print("下单后订单详情页显示商品数量：%s"%quantity_after)
            time.sleep(1)
            order_after = driver.find_element_by_id("order_id").text
            #order_after = int(order_after)
            print("下单后订单详情页显示订单号：%s"%order_after)
            time.sleep(1)
            #断言下单前与下单后的订单号、商品名称、价格、数量是否一致
            assert order_pre == order_after
            print("断言下单前与下单后的订单号一致")
            time.sleep(1)

            assert goods_name_pre == goods_name_after
            print("断言下单前与下单后的商品名称一致")
            time.sleep(1)
            try:
                assert price_pre == price_after
                print("断言下单前与下单后的总价格一致")
            except AssertionError as e:
                print("断言下单前与下单后的总价格不一致")
            time.sleep(1)
            try:
                assert Dn == quantity_after
                print("断言下单前与下单后的总数量一致")
            except AssertionError as e:

                print("断言下单前与下单后的总数量不一致")
            time.sleep(5)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(driver)
            raise










