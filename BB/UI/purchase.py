import unittest,time,sys
from testcase.models.function import Function

sys.path.append("../DATA")
from data_info import heaven_info

from login import TestLogin
from get_url import Url
from get_img import Img



class Testpurchase():
    def setUp(self):
        time.sleep(2)


    def testpurchase(self,driver,An,Bn,Cn,Dn,En,Fn,Gn,Hn,In,Jn):
        try:
            #顶部广告栏叉掉
            # driver.find_element_by_xpath ( "html/body/header/div[1]/i" ).click ()
            #--------------------用户登录--------------------------
            TestLogin().testlogin(driver,An,Bn)
            time.sleep(4)
            #----------------------首页-----------------------------
            # 搜索商品名称
            driver.find_element_by_id("searchInput").send_keys(Cn)
            time.sleep(3)
            #点search按钮
            driver.find_element_by_id("searchBtn").click()
            time.sleep(6)
            # 获得当前句柄
            sreach_windows =driver.current_window_handle
            #点击商品，打开新窗口
            driver.find_element_by_xpath("html/body/main/div[3]/div[3]/ul/li[1]/div[2]/a").click()
            time.sleep(3)
            # 返回当前所有打开的窗口的句柄
            all_handles = driver.window_handles
            # 定位当前最新窗口
            for handle in all_handles:
                if handle != sreach_windows:
                    driver.switch_to.window(handle)
                    time.sleep ( 3 )
                    #---------------进入商品详情页默认个数为1--------------------------------
                    #判断商品详情页：判断分支进入Add to Cart/Buy Now
                    if En == "Add to Cart":
                        #进入购物车
                        driver.find_element_by_id ( "add-to-cart" ).click ()
                        time.sleep(2)
                        # 将页面滚动条拖到顶部
                        js = "var q=document.body.scrollTop=0"
                        driver.execute_script ( js )
                        time.sleep ( 2 )
                        # 点shopping Cart
                        driver.find_element_by_xpath ( "html/body/header/div[2]/div/div/div[4]/div[1]/div" ).click ()
                        time.sleep ( 5 )
                        # 点proceed to checkout进入订单提交页checkout
                        driver.find_element_by_id ( "proceed_to_checkout" ).click ()
                        time.sleep ( 6 )
                    elif En == "Buy Now":
                        #很快佛Buy Now按钮
                        driver.find_element_by_id ( "buy-now" ).click ()

                    # 将页面滚动条拖到底部
                    js = "var q=document.body.scrollTop=1000"
                    driver.execute_script ( js )
                    time.sleep ( 2 )
                    #留言
                    driver.find_element_by_id("message").send_keys(Gn)
                    time.sleep(2)
                    #下单之前的商品数量
                    quantity_pre =int(driver.find_element_by_xpath("html/body/main/div[4]/div[2]/div[2]/div[2]/div/div[3]/p").text)
                    print ( "下单前商品数量：%s" % quantity_pre )
                    #提交订单
                    driver.find_element_by_id("submitOrder").click()
                    time.sleep(6)
                    #下单后Order Payment页面
                    #断言是否下单成功
                    assert "Order submitted !" == driver.find_element_by_xpath("html/body/main/div/div[1]").text
                    print("下单成功")
                    time.sleep ( 2 )

                    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
                    #点击View order items按钮
                    driver.find_element_by_id("itemsMore").click()
                    time.sleep ( 2 )
                    #获得订单后的商品名称\价格、数量及订单号
                    #商品名称
                    # goods_name_after = driver.find_element_by_xpath("html/body/main/div/div[4]/div/div[2]/div/div[1]/ul/li[1]/a").text
                    # print("下单后订单详情页显示商品名称：%s"%goods_name_after)
                    # time.sleep(1)
                    #商品价格
                    # price_after = driver.find_element_by_xpath("html/body/main/div/div[4]/div/div[2]/div/div[4]/p").text
                    # print("下单后订单详情页显示商品价格：%s"%price_after)
                    time.sleep(1)
                    #商品数量
                    quantity_after = driver.find_element_by_xpath("html/body/main/div/div[4]/div/div[2]/div/div[3]").text
                    quantity_after = int(quantity_after)
                    print("下单后订单详情页显示商品数量：%s"%quantity_after)
                    time.sleep(1)
                    #商品订单
                    order_after = driver.find_element_by_xpath("html/body/main/div/div[2]").text
                    str = order_after.split ( ':' )
                    #order_after = int(order_after)
                    print("下单后订单详情页显示订单号：%s"%str[1])
                    time.sleep(1)
                    #断言下单前与下单后的订单号、商品名称、价格、数量是否一致
                    # assert Cn == goods_name_after
                    # print("断言下单前与下单后的商品名称一致")
                    # time.sleep(1)

                    # assert price_pre == price_after
                    # print("断言下单前与下单后的总价格一致")

                    time.sleep(1)

                    assert quantity_pre == quantity_after
                    print("断言下单前与下单后的总数量一致")


        except Exception as msg:
            print(u"异常原因%s" % msg)
            Function().insert_img(driver)
            raise











