import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

sender_email = "your-email@gmail.com"
password = "your-password"
subject = "Internship Application"

with open("mail.txt", "r") as file:
    recipient_emails = [line.strip() for line in file.readlines()]

with open("letter.txt", "r") as letter_file:
    body = letter_file.read()

resume_path = "resume.pdf"

smtp_server = "smtp.gmail.com"
smtp_port = 465  

context = ssl.create_default_context()

for recipient_email in recipient_emails:
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        if os.path.exists(resume_path):
            with open(resume_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(resume_path)}",
                )
                message.attach(part)
        else:
            print(f"Resume file '{resume_path}' not found. Skipping attachment.")

        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"{recipient_email} - ✔ Done")
    
    except Exception as e:
        print(f"{recipient_email} - Error: {e}")
