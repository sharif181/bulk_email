import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from smtpd import COMMASPACE

username_pass = open("credential.txt").read().split('\n')
rec_emails = open("emails.txt").read().split('\n')
filename = open("file_name_with_extensions.txt").read().split('\n')
subject = open("email_subject.txt").read().split('\n')
body = open("email_body.txt").read()


msg = MIMEMultipart()
msg['From'] = username_pass[0]
msg['To'] = COMMASPACE.join(rec_emails)
msg['Subject'] = str(subject[0])

attachment = open(str(filename[0]), "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename[0])

msg.attach(part)

msg.attach(MIMEText(str(body), 'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username_pass[0], username_pass[1])
server.sendmail(username_pass[0], rec_emails, text)
server.close()
