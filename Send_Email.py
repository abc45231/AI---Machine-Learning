import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    senders_address = 'kannan2590@gmail.com'
    password = getpass.getpass()

    subject = 'AI -Machine Learning'

    msg = '''
    Hello Everyone !
    We are please to announce that we are going to start a new course of AI and Machine learning!

    Thank You!
    Kannan

    '''

    # Server initialization
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senders_address, password)
    recipients = ['kannan2590@gmail.com', 'kannan9025@yahoo.com']

    ##Draft

    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = senders_address
    msg['To'] = ", ".join(recipients)


    server.sendmail(senders_address, recipients, msg.as_string())


send_email()

