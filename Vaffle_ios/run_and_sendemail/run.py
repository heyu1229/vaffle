import unittest,os,time,smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner


mail_uesr='lisa.he@heavengifts.com'
mail_tolist=['beth.yu@heavengifts.com']
mail_password='aCuHUJ7gXM'#'7RH8TiwmK6'

def send_email(report,excel):
    file=open(report,'rb')
    mail_body=file.read()
    file.close()
    msgText=MIMEText(mail_body,'html','utf-8')
    msg=MIMEMultipart('related')
    msg['From']=mail_uesr
    msg['To']=';'.join(mail_tolist)
    msg['Subject']=Header('IOS vaffle2.4.3 ios手机自动化测试报告','utf-8')
    msg.attach(msgText)
    #添加excel附件
    excelatt=MIMEApplication(open('%s'%excel,'rb').read())
    excelatt.add_header('Content-Disposition','attachment',filename=excel)
    msg.attach(excelatt)
    #添加测试报告附件
    reportatt=MIMEApplication(open('%s'%report,'rb').read())
    reportatt.add_header('Content-Disposition','attachment',filename=report)
    msg.attach(reportatt)
    flag=True
    try:
        server=smtplib.SMTP('mail.heavengifts.com',25)
        server.login(mail_uesr,mail_password)
        server.sendmail(mail_uesr,mail_tolist,msg.as_string())
        server.close()
    except Exception as e:
        print('Error:',e)
        flag=False
    return flag

#查询最新生成的测试报告
def new_report(testreport):
    list=os.listdir(testreport)
    list.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
    report=os.path.join(testreport,list[-1])
    return report

#查询最新生成的excel文档
def new_excel(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "/" + fn))
    excel = os.path.join(testreport,lists[-1])
    return excel


if __name__ == '__main__':
    # 用例地址
    test_dir = "..//testcase"
    # 测试报告存放地址
    test_report = "..//testreport"
    # 最新接口excel
    test_excel = "..//testdata"

    # 查看用例地址中用例
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='testcase003*.py', top_level_dir=None)
    # 获取现在的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 定义文件名
    # 定义文件名
    filename = test_report + "/" + now + "result.html"
    print("filename %s" % filename)
    # 用web形式打开文件
    fp = open(filename, 'wb')

    # 定义网页测试报告的标题和副标题
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
    # runner = HTMLTestRunner
    # 在网页中显示运行所有测试用例的结果
    runner.run(discover)
    fp.close()
    # 创建要一个新报告继承测试报告
    new_report = new_report(test_report)
    new_excel = new_excel(test_excel)
    # 发送测试报告
    if send_email(new_report, new_excel):
        print('发送邮件成功')
    else:
        print('发送邮件失败')