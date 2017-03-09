__author__ = 'Bnizzle'
import os, datetime, smtplib
import config
username = config.username
password = config.password
MESSAGE_FORMAT = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" # %(fromAddr,to,subject,text)


def sendEmail(recipient, message):
    SMTP_SERVER_URL = 'smtp.gmail.com:587'
    mailserver = smtplib.SMTP(SMTP_SERVER_URL)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(username, password)
    mailserver.sendmail('', recipient, message)
    mailserver.close()


def sendEmailWithFields(to, subject, text):
    message = MESSAGE_FORMAT%('', to, subject, text)
    sendEmail(to, message)


def logDownStatus(status_code):
    filename1 = datetime.datetime.now().strftime("%Y%m%d")
    path = 'Logs'
    with open(os.path.join(path, filename1) + '.txt', 'a') as f:
        f.writelines('\n' + datetime.datetime.now().strftime("%H:%M:%S") + ' - ' + str(status_code))
