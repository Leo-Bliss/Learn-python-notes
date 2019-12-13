#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/12 0012 23:49
#@Author  :    tb_youth
#@FileName:    SendEmail.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
使用smtplib模块实现带附件发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



from_address = '15270684004@163.com'
password = 'tbyouth666'

to_address = '2638961251@qq.com'
smtp_server = 'smtp.163.com'

#可带附件的邮件
new_msg = MIMEMultipart()
new_msg.attach(MIMEText('附件'))

#邮件内容
#主题
new_msg['Subject'] = '科研实践项目反馈邮件'

new_msg['From'] = from_address
new_msg['To'] = to_address
#读入附件内容
with open('./test.txt','r',encoding='utf-8') as f:
       att_file = f.read()
attach = MIMEText(att_file)
attach['Content-type'] = 'appliction/octet-stream'
attach['Content-Disposition'] = 'attachment;filename="666.txt"'
new_msg.attach(attach)

server = smtplib.SMTP(smtp_server,port=25)
server.set_debuglevel(1)
server.login(from_address,password)
try:
    server.sendmail(from_address,to_address,new_msg.as_string())
    server.quit()
    print('发送成功！')
except Exception as e:
    print('出错啦~')
    print(e)



