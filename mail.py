# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

sender = 'mrzhencc@sina.com'
receiver = 'zhenchao@easted.com.cn'


def mail():
    ret = True
    try:
        msg = MIMEText('你好，这是第一封邮件', 'plain', 'utf-8')
        msg['From'] = formataddr(['zhenc', sender])
        msg['To'] = formataddr(['chao', receiver])
        msg['Subject'] = 'test mail'

        server = smtplib.SMTP('smtp.sina.com', 25)
        server.login(sender, '625210chao')
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
    except:
        ret = False

    return ret

_ret = mail()
if _ret:
    print "success"
else:
    print "error"
