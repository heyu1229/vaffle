import unittest,time,os,smtplib,sys
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart

my_sender='lisa.he@heavengifts.com' #发件人邮箱账号
my_user='omv.team@heavengifts.com' #收件人邮箱账号
# my_user='1004856404@qq.com' #收件人邮箱账号
#发送邮件
def send_mail(file_new,excel_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    ret=True
    try:
        msg = MIMEMultipart('related')
        msg["From"] = my_sender
        msgText = MIMEText(mail_body,'html','utf-8')
        msg['Subject'] = Header('vaffle 2.4.1 develop接口自动化测试报告','utf-8')
        msg.attach(msgText)

        # #添加excel附件
        # att = MIMEText(open('%s' % excel_new, 'rb').read(), 'base64', 'gb2312')
        # att["Content-Type"] = 'application/octet-stream'
        # att["Content-Disposition"] = 'attachment; filename="%s"' % excel_new
        # msg.attach(att)

        xlsxpart = MIMEApplication(open('%s' % excel_new, 'rb').read () )
        xlsxpart.add_header ( 'Content-Disposition', 'attachment', filename=excel_new )
        msg.attach ( xlsxpart )
        #添加测试报告附件
        # att = MIMEText(open('%s' % file_new, 'rb').read(), 'base64', 'utf-8')
        # att["Content-Type"] = 'application/oc1tet-stream'
        # att["Content-Disposition"] = 'attachment; filename="%s"' % file_new
        # msg.attach(att)

        att = MIMEApplication(open('%s' % file_new, 'rb').read () )
        att.add_header ( 'Content-Disposition', 'attachment', filename=file_new )
        msg.attach ( att )


        server = smtplib.SMTP("mail.heavengifts.com",25)
        server.login(my_sender,"aCuHUJ7gXM")
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.close()
    except Exception as e:#如果try中的语句没有执行，则会执行下面的ret=False
        print('error:',e)
        ret=False
    return ret



#查询最新生成的测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
    file_new = os.path.join(testreport,lists[-1])
    # print(file_new)
    return file_new

#查询最新生成的excel文档
def new_excel(testreport):

    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
    excel_new = os.path.join(testreport,lists[-1])
    return excel_new

if __name__ == '__main__':

    #用例地址
    print(os.getcwd())
    test_dir = os.getcwd()[:-9]+"/testcase"
    print("test_dir:%s" %test_dir)
    #测试报告存放地址
    test_report = os.getcwd()[:-9]+"/test_report"
    #最新接口excel
    test_excel = os.getcwd()[:-9]+"/test_date"

    #查看用例地址中用例
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*.py', top_level_dir=None)
    #获取现在的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #定义文件名
    filename = test_report + "/" + now + "result.html"
    print("filename %s" %filename)
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

    new_excel = new_excel(test_excel)

    #发送测试报告
    send_mail(new_report,new_excel)

