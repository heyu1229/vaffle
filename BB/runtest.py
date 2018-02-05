import unittest,time,os,smtplib,sys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.header import Header
from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart

from PIL import Image
from UI.get_img import Img

sys.path.append('./UI')
sys.path.append('./DB')
from sql_search import SQL_SEARCH_1
from sql_hg import SQL_HG
sys.path.append('./report')
sys.path.append('./testcase')
sys.path.append("./DATA")
sys.path.append('./img')
my_sender='lisa.he@heavengifts.com' #发件人邮箱账号
# my_user='bb.team@heavengifts.com' #收件人邮箱账号
my_user='1004856404@qq.com' #收件人邮箱账号
#my_user='tasia.feng@heavengifts.com' #收件人邮箱账号

#发送邮件
def send_mail(file_new,img_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    ret=True
    try:
        msg = MIMEMultipart('related')
        msg["From"] = my_sender
        msgText = MIMEText(mail_body,'html','utf-8')
        msg['Subject'] = Header('BuyBest正式环境自动化测试报告','utf-8')
        msg.attach(msgText)

        # jpg类型附件
        part = MIMEImage(open('%s' % img_new, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="%s" % img_new)
        msg.attach(part)

        #添加测试报告附件
        att = MIMEApplication(open('%s' % file_new, 'rb').read () )
        att.add_header ( 'Content-Disposition', 'attachment', filename=file_new )
        msg.attach (att)

        server = smtplib.SMTP("mail.heavengifts.com",25)
        server.login(my_sender,"aCuHUJ7gXM")
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.quit()
    except Exception as e:   #如果try中的语句没有执行，则会执行下面的ret=False
        print(e)
        ret=False
    return ret


#查询最新生成的测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

#查询最新生成的错误图片
def new_img(testreport):
    #
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    img_new = os.path.join(testreport,lists[-1])
    print(img_new)
    return img_new


if __name__ == '__main__':

    #用例地址
    test_dir = "./testcase"
    
    #测试报告存放地址
    test_report = "./report"

    #抛出异常截图
    test_img = "./img"


    #add_order = get_AddOrder().test_add_order()
    sql = SQL_HG().get_task_add_order1()

    auto_type = '%s' % SQL_SEARCH_1().search(sql)
    #执行自动下单
    # congratulations成为最新图片
    nowTime = time.strftime ( "%Y%m%d.%H.%M.%S" )
    success_image = Img ().test_success_image ()
    img = Image.open ( success_image + "congratulations.png" )
    # 保存图像为png格式
    img.save ( success_image + 'sucess_%s.png' % nowTime, "png" )

    #查看所有用例
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    #discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_03*.py')
    #获取现在的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    
    #定义文件名
    filename = test_report + "\\" + now + "result.html"
    
    #用web形式打开文件
    fp = open(filename,'wb')
    
    #定义网页测试报告的标题和副标题
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况：')
    
    #在网页中显示运行所有测试用例的结果
    runner.run(discover)
    fp.close()

    #创建要一个新报告继承测试报告
    new_report = new_report(test_report)
    new_img = new_img(test_img)

    #发送测试报告
    send_mail(new_report,new_img)

