import smtplib  
import os  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email import encoders  
user = "1483265434@qq.com"
pwd = "zvtqwungfqixjahh"
to = ['quan.liu@decheche.com']
msg = MIMEMultipart()  
msg['Subject'] = '这里是主题...'  
content1 = MIMEText('这里是正文！', 'html', 'utf-8')
msg.attach(content1)  
attfile = './report/api_test_report.html'
basename = os.path.basename(attfile)  
fp = open(attfile, 'rb')  
att = MIMEText(fp.read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))  
#encoders.encode_base64(att)
msg.attach(att)  
#-----------------------------------------------------------  
s = smtplib.SMTP_SSL("smtp.qq.com", 465)
s.login(user, pwd)  
s.sendmail(user, to, msg.as_string())  
print('发送成功')  
s.close()  