from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"]="Anonymous fan"
message["to"]="42nikolatesla@gmail.com"
message["subject"]="A message from Anonymous"
message.attach(MIMEText(
    'In 2011, Anonymous played a significant role in supporting the Arab Spring uprisings, using cyberattacks to '
    'disrupt government websites and spread information about the protests. They also targeted companies doing '
    'business with repressive regimes.'))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("nlanfupaswan42@gmail.com", "nandu@8268321156")
    smtp.send_message(message)
    print("sent............")
