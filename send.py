import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Replace with your email credentials
sender_email = "muhd.akram1024@gmail.com"
password = "347368919"
subject = "Internship Application"

# Read the email list from the file
with open("mail.txt", "r") as file:
    recipient_emails = [line.strip() for line in file.readlines()]

# Read the letter content from letter.txt
with open("letter.txt", "r") as letter_file:
    body = letter_file.read()

# Path to the resume PDF file
resume_path = "resume.pdf"

# Set up the server (For Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 465  # SSL port

# Create a secure SSL context
context = ssl.create_default_context()

# Send email to each recipient in the list
for recipient_email in recipient_emails:
    try:
        # Create a MIMEText object for the email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Attach the resume.pdf file
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

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"{recipient_email} - ✔ Done")
    
    except Exception as e:
        print(f"{recipient_email} - Error: {e}")
