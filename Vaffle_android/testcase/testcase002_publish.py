import os
import unittest,time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from public.installapp import androidtest
from public.publicway import Publicway
from public.readdata import Readdata
from public.writedata import Writedata
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class AndroidTest_publish(unittest.TestCase):

    def setUp(self):
        os.system ( 'start startAppiumServer.bat' )
        time.sleep ( 10 )
        Android = androidtest()
        self.driver=Android.android()
        self.public=Publicway(self.driver)
        self.read = Readdata()
        self.write = Writedata()
        self.user = self.read.Read_data(0, 1, 0)
        self.password = int(self.read.Read_data(0, 1, 1))
    #-----------------------发纯文本POST---------------------------------------------
    def testcase001_post_text(self):
        print(self.user, self.password)
        #登录用户
        self.public.login_vaffle(self.user, self.password)
        #点击发布按钮
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_publish').click()
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        #点允许直接进入相册页面
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        # except:
        #     print("no alter")

        #选择第一张照片后删除,再输入纯文本
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[1].click()#选择第一张照片
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/iv_select").click() #打勾
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/img_pix_delete").click() #删除已选图片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/share_to_et').send_keys(date + ' auto test post text') #输入纯文本
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_toolbar_right').click()

        # self.public.swipeDown(5)
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_me').click()  #进入Me页面

        self.driver.find_element_by_id('com.heavengifts.vaffle:id/cnt_posts').click() #进入POSTS页面

        # post = self.driver.find_element_by_id('com.heavengifts.vaffle:id/home_recyclerview')
        # posts = post.find_elements_by_class_name('android.widget.LinearLayout')
        # post_detail = posts[0].find_element_by_id('com.heavengifts.vaffle:id/item_post_head_layout')
        text = self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_content').text
        print(text)
        self.assertEqual(text, date + ' auto test post text',self.write.Write_data(1,1,4,'发布失败'))
        self.write.Write_data(1,1,4,'发布成功')


    #-----------------------发拍照片的POST---------------------------------------------
    def testcase002_post_takeonephoto(self):
        print(self.user, self.password)
        self.public.login_vaffle(self.user, self.password)
        #点击发布按钮
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_publish').click()
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        #点允许直接进入相册页面
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        # except:
        #     print("no alter")
        # self.driver.execute_script ( "mobile: tap", {"touchCount": "1", "x": 177, "y": 390} )
        #拍照发POST
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[0].click()#拍照
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#允许访问相机或录制视频
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#允许访问麦克风
        # except:
        #     print("no alter")
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/view_photo_video_select').click()#点击拍照
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/view_operate_done').click() #点击提交照片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":1002, "y":131})  #确定发布
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/share_to_et').send_keys(date + ' auto test post take one photo') #输入文本
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_toolbar_right').click() #确定发布
        #显示等待your post is being sent now消失
        #WebDriverWait(self.driver,15).until_not(EC.visibility_of_element_located((By.ID,"com.heavengifts.vaffle:id/ll_post")))
        WebDriverWait(self.driver, 40).until_not(
            lambda driver: driver.find_element_by_id("com.heavengifts.vaffle:id/ll_post"))

        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_me').click()  #进入Me页面
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/cnt_posts').click() #进入POSTS页面

        text = self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_content').text
        print(text)
        self.assertEqual(text, date + ' auto test post take one photo')
        if self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_image').is_displayed():
            viewgroup = self.driver.find_element_by_id('com.heavengifts.vaffle:id/rel_image1')
            images = viewgroup.find_elements_by_class_name('android.widget.ImageView')
            self.assertEqual(1, len(images), self.write.Write_data(1, 2, 4, '发布拍摄一张图片失败'))
            self.write.Write_data(1, 2, 4, '发布成功')
        else:
            print('发布拍摄一张图片失败')
        time.sleep(2)


    #-----------------------发布编辑后的图片的POST---------------------------------------------
    def testcase003_post_edit_photo(self):
        print(self.user, self.password)
        self.public.login_vaffle(self.user, self.password)
        #点击发布按钮
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_publish').click()
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        #点允许直接进入相册页面
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        # except:
        #     print("no alter")

        #选择第一张照片编辑后发POST
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[1].find_element_by_id('com.heavengifts.vaffle:id/frameLayout').click()#选择第一张照片
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_select').click() #点击提交照片
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/post_image_edit' ).click ()  # edit photo，进入编辑图片页面
        filtersView = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/edit_recyclerView' )
        filters = filtersView.find_elements_by_class_name("android.widget.LinearLayout")
        filters[1].find_element_by_id ( 'com.heavengifts.vaffle:id/filter_image').click() #选择第二个滤镜
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/tv_tool").click() #进入裁剪页面
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/iv_rotate" ).click ()#旋转90度
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/iv_cropped" ).click ()  # 裁剪
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/iv_crop_complete" ).click ()  # 裁剪打勾
        self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/tv_done" ).click ()  # Done，图片编辑成功
        # main_frame = self.driver.find_element_by_id("com.heavengifts.vaffle:id/main_frame")
        # aa = main_frame.find_elements_by_class_name("android.widget.RelativeLayout")
        # aa[2].send_keys (' auto test post take an edited photo' )  # 输入文本
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/share_to_et').send_keys(date + ' auto test post take an edited photo') #输入文本
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_toolbar_right').click() #确定发布
        # self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":1002, "y":131})  #确定发布
        # time.sleep(3)s
        # 显示等待your post is being sent now消失
        WebDriverWait(self.driver,40).until_not(EC.visibility_of_element_located((By.ID,"com.heavengifts.vaffle:id/ll_post")))
        # WebDriverWait(self.driver, 40).until_not(
        #     lambda driver: driver.find_element_by_id("com.heavengifts.vaffle:id/ll_post"))
        self.public.swipeDown(2000)

        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_me').click()  #进入Me页面

        self.driver.find_element_by_id('com.heavengifts.vaffle:id/cnt_posts').click() #进入POSTS页面
        text = self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_content').text
        print(text)
        self.assertEqual(text, date + ' auto test post take an edited photo')
        if self.driver.find_element_by_id('com.heavengifts.vaffle:id/item_post_image').is_displayed():
            viewgroup = self.driver.find_element_by_id('com.heavengifts.vaffle:id/rel_image1')
            images = viewgroup.find_elements_by_class_name('android.widget.ImageView')
            self.assertEqual(1, len(images), self.write.Write_data(1, 3, 4, '发布编辑后的图片失败'))
            self.write.Write_data(1, 3, 4, '发布成功')
        else:
            print('发布编辑后的图片失败')
        time.sleep(2)

      #拍9张图片发POST
    def testcase004_post_takeninephotos(self):
        self.driver.implicitly_wait(20)
        print(self.user, self.password)
        self.public.login_vaffle(self.user, self.password)
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_publish').click()  #点击发布
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        #点允许直接进入相册页面
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

        # except:
        #     print("no alter")
        #拍照发POST
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[0].click()#拍照
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#允许访问相机或录制视频
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#允许访问麦克风
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/view_photo_video_select').click()#点击拍照
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/view_operate_done').click() #点击提交照片
        #循环点击8次拍摄照片
        for n in range(1,9):
            self.driver.find_element_by_id('com.heavengifts.vaffle:id/publish_photo_media').click()
            photoes[0].click()
            self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_photo_video_select' ).click ()  # 点击拍照
            self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_operate_done' ).click ()  # 点击提交照片

        date = time.strftime ( '%Y-%m-%d %H:%M:%S', time.localtime () )
        # self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":1002, "y":131})  #确定发布
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/share_to_et' ).send_keys (
            date + ' auto test post take one photo' )  # 输入文本
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/iv_toolbar_right' ).click ()  # 确定发布

        # 显示等待your post is being sent now消失
        WebDriverWait(self.driver,120).until_not(EC.visibility_of_element_located((By.ID,"com.heavengifts.vaffle:id/ll_post")))
        # WebDriverWait(self.driver, 80).until_not(
        #     lambda driver: driver.find_element_by_id("com.heavengifts.vaffle:id/ll_post"))
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/bottom_menu_me' ).click ()  # 进入Me页面
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/cnt_posts' ).click ()  # 进入POSTS页面
        text = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/item_post_content' ).text
        self.assertEqual ( text, date + ' auto test post take one photo' )
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/item_post_head_layout").click() #进入该post详情页
        if self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_post_detail_grid' ).is_displayed ():
            viewgroup = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_post_detail_grid' )
            images = viewgroup.find_elements_by_class_name ( 'android.widget.ImageView' )
            self.assertEqual ( 9, len ( images ), self.write.Write_data ( 1, 4, 4, '发布拍摄九张图片失败' ) )
            self.write.Write_data ( 1, 4, 4, '发布成功' )
        else:
            print ( '发布拍摄九张图片失败' )
        time.sleep ( 2 )

       # 选择9张图片发POST
    def testcase005_post_select_ninephotos(self):
        print ( self.user, self.password )
        self.public.login_vaffle ( self.user, self.password )
        # 点击发布按钮
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/bottom_menu_publish' ).click ()
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        # 点允许直接进入相册页面
        self.driver.find_element_by_id ( "com.android.packageinstaller:id/permission_allow_button" ).click ()
        # except:
        #     print("no alter")

        # 选择第一张照片编辑后发POST
        library = self.driver.find_element_by_id ( "com.heavengifts.vaffle:id/library_grid" )
        photoes = library.find_elements_by_class_name ( 'android.widget.FrameLayout' )
        for n in range(1,10):
            photoes[n].find_element_by_id ( 'com.heavengifts.vaffle:id/frameLayout' ).click()# 选择9 张照片
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_select').click() # 点击提交照片
        date = time.strftime ( '%Y-%m-%d %H:%M:%S', time.localtime () )
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/share_to_et' ).send_keys (
            date + ' auto test post select nine photos' )  # 输入文本
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/iv_toolbar_right' ).click ()  # 确定发布
        # self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":1002, "y":131})  #确定发布
        # time.sleep(3)s
        # 显示等待your post is being sent now消失
        WebDriverWait(self.driver,120).until_not(EC.visibility_of_element_located((By.ID,"com.heavengifts.vaffle:id/ll_post")))
        # WebDriverWait(self.driver, 40).until_not(
        #     lambda driver: driver.find_element_by_id("com.heavengifts.vaffle:id/ll_post"))
        self.public.swipeDown ( 2000 )

        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/bottom_menu_me' ).click ()  # 进入Me页面
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/cnt_posts' ).click ()  # 进入POSTS页面
        text = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/item_post_content' ).text
        self.assertEqual ( text, date + ' auto test post select nine photos' )
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/item_post_head_layout").click() #进入该post详情页
        if self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_post_detail_grid' ).is_displayed ():
            viewgroup = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/view_post_detail_grid' )
            images = viewgroup.find_elements_by_class_name ( 'android.widget.ImageView' )
            self.assertEqual ( 9, len ( images ), self.write.Write_data ( 1, 5, 4, '发布选择相册的九张图片失败' ) )
            self.write.Write_data ( 1, 5, 4, '发布成功' )
        else:
            print ( '发布选择相册的九张图片失败' )
        time.sleep ( 2 )


      #录视频发POST
    def testcase006_post_takevideo(self):
        self.driver.implicitly_wait(20)
        print(self.user, self.password)
        self.public.login_vaffle(self.user, self.password)
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_publish').click()  #点击发布
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        #点允许直接进入相册页面
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

        # except:
        #     print("no alter")
        #拍照发POST
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[0].click()#拍照
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#允许访问相机或录制视频
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()#允许访问麦克风
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/view_photo").click() #切换视频
        action1 = TouchAction ( self.driver )
        el = self.driver.find_element_by_id("com.heavengifts.vaffle:id/view_photo_video_select")
        action1.long_press ( el,None,None,10000 ).perform ()
        self.driver.find_element_by_id("com.heavengifts.vaffle:id/view_operate_done").click()  #视频确认
        date = time.strftime ( '%Y-%m-%d %H:%M:%S', time.localtime () )
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/share_to_et' ).send_keys (
            date + ' auto test post take video' )  # 输入文本
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/iv_toolbar_right' ).click ()  # 确定发布

        # 显示等待your post is being sent now消失
        WebDriverWait(self.driver,120).until_not(EC.visibility_of_element_located((By.ID,"com.heavengifts.vaffle:id/ll_post")))
        # WebDriverWait(self.driver, 80).until_not(
        #     lambda driver: driver.find_element_by_id("com.heavengifts.vaffle:id/ll_post"))
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/bottom_menu_me' ).click ()  # 进入Me页面
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/cnt_posts' ).click ()  # 进入POSTS页面
        text = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/item_post_content' ).text

        if text:
            self.assertEqual ( text, date + ' auto test post take video' )
            self.write.Write_data ( 1, 6, 4, '发布成功' )
        else:
            self.write.Write_data ( 1, 6, 4, '发布失败' )

    #-----------------------发布已选视频---------------------------------------------
    def testcase007_post_select_video(self):
        print(self.user, self.password)
        self.public.login_vaffle(self.user, self.password)
        #点击发布按钮
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/bottom_menu_publish').click()
        # try:
        #     if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container").is_displayed():
        #点允许直接进入相册页面
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        # except:
        #     print("no alter")

        #选择第一张照片编辑后发POST
        library = self.driver.find_element_by_id("com.heavengifts.vaffle:id/library_grid")
        photoes = library.find_elements_by_class_name('android.widget.FrameLayout')
        photoes[1].find_element_by_id('com.heavengifts.vaffle:id/frameLayout').click()#选择video
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_select').click() #点击提交照片
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/share_to_et').send_keys(date + ' auto test post select video') #输入文本
        self.driver.find_element_by_id('com.heavengifts.vaffle:id/iv_toolbar_right').click() #确定发布
        # 显示等待your post is being sent now消失
        WebDriverWait(self.driver,120).until_not(EC.visibility_of_element_located((By.ID,"com.heavengifts.vaffle:id/ll_post")))
        # WebDriverWait(self.driver, 80).until_not(
        #     lambda driver: driver.find_element_by_id("com.heavengifts.vaffle:id/ll_post"))
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/bottom_menu_me' ).click ()  # 进入Me页面
        self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/cnt_posts' ).click ()  # 进入POSTS页面
        text = self.driver.find_element_by_id ( 'com.heavengifts.vaffle:id/item_post_content' ).text

        if text:
            self.assertEqual ( text, date + ' auto test post select video' )
            self.write.Write_data ( 1, 7, 4, '发布成功' )
        else:
            self.write.Write_data ( 1, 7, 4, '发布失败' )
        time.sleep(2)

    def tearDown(self):
        os.system ( 'start stopAppiumServer.bat' )
        time.sleep(20)
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()