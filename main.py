import json
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Sender:
    def __init__(self, senderEmail, recieverEmail):
        self.config = json.loads(open("config.json", "r").read())
        self.senderEmail = senderEmail
        self.recieverEmail = recieverEmail

        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(senderEmail, self.config['googlepassword'])

        self.text = f"Subject: {self.config['subject']}\n\n{self.config['message']}"

    def sendMail(self):
        if self.config['html']:
            plain = MIMEText(self.text, 'plain')
            html = MIMEText(open('html/email.html', 'r').read(), 'html')

            message = MIMEMultipart('alternative')
            message['Subject'] = "Link"
            message['From'] = self.senderEmail
            message['To'] = self.recieverEmail
            message.attach(plain)
            message.attach(html)

            self.text = message.as_string()

        self.server.sendmail(self.senderEmail, self.recieverEmail, self.text)

        print(f"-> Sent Email to: {self.recieverEmail}")


Sender("shardz60fps@gmail.com", "afilityx@gmail.com").sendMail()