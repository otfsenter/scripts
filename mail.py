#!/usr/bin/env python
# coding: utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Import the email modules we'll need
import my_key

username = my_key.my_username
password = my_key.my_password

me = '123@gmail.com'
you = '123@gmail.com'
body_detail = """
<p>123</p>

<p>456</p>

<p>123</p>
"""

attachment = 'bppm.docx'
# attachment = 'name.txt'

pic = 'alice.png'


msg = MIMEMultipart()
body = MIMEText(body_detail, 'html', 'utf-8')
msg.attach(body)


files = MIMEText(open(attachment, 'rb').read(), 'html', 'utf-8')
files["Content-Type"] = 'application/octet-stream'
files["Content-Disposition"] = "attachment;filename=%s" % attachment
msg.attach(files)


image = open(pic, 'rb')
read_image = MIMEImage(image.read())
image.close()
read_image.add_header('Content-ID', '<image%s>' % str(len(pic)))
msg.attach(read_image)


msg['Subject'] = 'subject'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.email.com', '25')
s.login(user=username, password=password)
s.send_message(msg)
s.quit()
