#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/13 0013 13:49
#@Author  :    tb_youth
#@FileName:    SendEmail0.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth


#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/12 0012 23:49
#@Author  :    tb_youth
#@FileName:    SendEmail.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
使用smtplib模块实现发送邮件
'''
import smtplib
from email.mime.text import MIMEText




from_address = '15270684004@163.com'
password = 'tbyouth666'

to_address = '2638961251@qq.com'
smtp_server = 'smtp.163.com'



#邮件内容
content = '科研实践2333'
new_msg = MIMEText(content,'plain','utf-8')

#主题
new_msg['Subject'] = '科研实践项目反馈邮件'
new_msg['From'] = from_address
new_msg['To'] = to_address


try:
    server = smtplib.SMTP(smtp_server, port=25)
    server.set_debuglevel(1)
    server.login(from_address, password)
    server.sendmail(from_address,to_address,new_msg.as_string())
    server.quit()
    print('发送成功！')
except Exception as e:
    print('出错啦~')
    print(e)



