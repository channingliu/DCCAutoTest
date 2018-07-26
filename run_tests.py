#！ /usr/bin/env python
#coding:utf-8

import time,os,sys
from HTMLTestRunner import HTMLTestRunner
import unittest
from email.mime.text import MIMEText #定义邮件内容
from email.header import Header #邮件主题
from email.mime.multipart import MIMEMultipart #附件
import smtplib
#from email import encoders

def send_mail(filename):
    mail_host = 'stmp.qq.com'
    mail_user = "1483265434@qq.com"
    #mail_pass = "okqwiahiuvwjhdig"
    mail_pass= "zvtqwungfqixjahh"
    sender = "测试专家权权" #发送邮箱别名（用户名）
    receivers=['quan.liu@decheche.com'] #收件人列表
    message = MIMEMultipart('related') #采用related定义内嵌资源的邮件体 （附件）

    #发送内容
    f = open(filename, 'rb')
    mail_body = f.read()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename= os.path.basename(filename))
    #encoders.encode_base64(att) 加密
    message.attach(att)
    f.close()




    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    message.attach(msg)
    message['From']=sender
    message["To"] =','.join(receivers)
    message['Subject'] = Header("接口自动化测试报告","utf-8")
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(mail_user,receivers,message.as_string())
    smtp.quit()

    #查找最新的测试报告
def report(testreport):
    lists = os.listdir(testreport)  # 返回指定文件夹下的文件或文件夹名称列表
    lists.sort(key=lambda fn: os.path.getatime(testreport + "/" + fn))  # 通过sort()方法按时间排序
    lists.reverse()
    filename = os.path.join(testreport, lists[0])
    print(filename,"发送成功")
    return filename




if __name__=="__main__":
    #api_test_data.init_data() #初始化接口测试数据
    # 指定测试用例为当前文件夹下的test_case目录
    test_dir = './api_test_case'
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='ddtDemo.py')

    now = time.strftime("%Y%m%d%H%M%S")
    filename = './report/'+now+'_api_test_report.html'
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,
                            title="DCC Auto Test  Report",
                            description="DCCAutoTest")
    runner.run(discover)
    fp.close()

    test_report = './report' #定义报告文件目录
    rep=report(test_report)
    send_mail(rep)
