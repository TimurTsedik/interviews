import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Mail:

    def __init__(self, login, password, recipients, subject, message):
        self.login = login
        self.password = password
        self.recipients = recipients
        self.subject = subject
        self.message = message
        self.smtp_address = "smtp.gmail.com"
        self.imap_address = "imap.gmail.com"
        self.header = None

    def send_mail(self):
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(self.recipients)
        message['Subject'] = self.subject
        message.attach(MIMEText(self.message))
        msg_sender = smtplib.SMTP(self.smtp_address, 587)
        # identify ourselves to smtp gmail client
        msg_sender.ehlo()
        # secure our email with tls encryption
        msg_sender.starttls()
        # re-identify ourselves as an encrypted connection
        msg_sender.ehlo()
        msg_sender.login(self.login, self.password)
        msg_sender.sendmail(self.login, self.recipients, message.as_string())
        msg_sender.quit()

    def receive_mail(self) -> str:
        msg_receiver = imaplib.IMAP4_SSL(self.imap_address)
        msg_receiver.login(self.login, self.password)
        msg_receiver.list()
        msg_receiver.select("inbox")
        criteria = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        data = msg_receiver.uid('search', None, criteria)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        data = msg_receiver.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        msg_receiver.logout()
        return email_message.as_string()


login = 'login@gmail.com'
password = 'qwerty'
subject = 'Subject'
recipients = ['vasya@email.com', 'petya@email.com']
message = 'Message'
mail = Mail(login, password, recipients, subject, message)
mail.send_mail()
print(mail.receive_mail())
