import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Sending email using smtplib 
# Created an object of email message
# and added content to that email
html = Template(Path('./index.html').read_text())
email = EmailMessage()
email['From'] = 'Yash Bhardwaj'
email['To'] = 'sumitsoni2666@gmail.com'
email['Subject'] = 'Test email'

email_id = 'byash2299@gmail.com'
email_pass = 'jcokdvjzgedzoalp'

email.set_content(html.substitute(name = 'Sumit'), 'html')

# Used gmail smtp host for sending email
with smtplib.SMTP(host = 'smtp.gmail.com',port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_id, email_pass)
    smtp.send_message(email)
    print('All good boss!')
