import smtplib
from email.message import EmailMessage

from email_template.export import email_template

EMAIL_ADDRESS = 'vlad.calin.theo@gmail.com'
EMAIL_PASSWORD = 'Nikeul1q2w3e'

RECIPIENT = 'calinvladth@icloud.com'

EMAIL_TEMPLATE = email_template
print('SENDING EMAIL')

msg = EmailMessage()
msg['Subject'] = 'Hola subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECIPIENT
msg.set_content('Hola, this is a subject')

msg.add_alternative(EMAIL_TEMPLATE, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print('SENT!')
