import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

'''
作者：pk哥
公众号：brucepk
日期：2018/10/20文档分类
代码解析详见公众号「brucepk」。

如有疑问或需转载，请联系微信号：dyw520520，备注来意，谢谢。
如需加入python技术交流群，请加我微信，备注「进群」，我拉你进群，一起讨论交流，共同成长。
'''

my_sender = 'xxx@qq.com'  # 发件人邮箱账号
my_user = 'xxx@qq.com'  # 收件人邮箱账号


def send_mail(mail_title, mail_content):
    try:
        '''发送邮件'''
        msg = MIMEText(mail_content, "plain", 'utf-8')  # 发送邮件内容
        msg["Subject"] = Header(mail_title, 'utf-8')  # 发送邮件主题/标题
        msg["From"] = formataddr(['Bruce Lee', my_sender])  # 邮件发送方
        msg["To"] = formataddr(['brucepk', my_user])  # 邮件接收方

        s = smtplib.SMTP("smtp.qq.com", 25)  # 邮箱的传输协议，端口默认25
        s.login(my_sender, 'xxxxxxxx')  # 登录邮箱，这里的第二个参数为qq邮箱授权码，不要填你的登录密码
        s.sendmail(my_sender, [my_user, ], msg.as_string())  # 发送方，接收方，发送消息
        s.quit()  # 退出邮箱
        print("邮件发送成功！")
    except Exception:
        print("邮件发送失败~~")


mail_title = '报告2'
mail_content = '报告内容2'
send_mail(mail_title, mail_content)
