# 📧 Bulk Internship Application Email Sender  

This Python script automates sending internship application emails to multiple recipients. It reads a list of email addresses from a file, attaches a resume, and sends personalized emails using SMTP.  

## 🚀 Features  
✅ Send emails to multiple recipients from a list  
✅ Attach a resume (PDF format)  
✅ Secure connection using SSL  
✅ Reads email content from a text file  

---

## 📜 Requirements  

Before running the script, ensure you have the following:  

- Python 3.x installed  
- A Gmail account with **Less Secure Apps access enabled** or **App Passwords configured**  
- The required Python libraries installed:  

```sh
pip install smtplib ssl email
```

---

## 📂 File Structure  

```
📂 bulk-email-sender  
├── mail.txt         # List of recipient email addresses (one per line)  
├── letter.txt       # Cover letter content (plain text)  
├── resume.pdf       # Your resume (PDF format)  
└── send.py          # Python script to send emails  
```

---

## ⚙️ Usage  

1️⃣ **Clone the repository**  
```sh
git clone https://github.com/ghostuser-bug/Email-Blaster.git
cd Email-Blaster
```

2️⃣ **Edit your email credentials** in `send.py`  
Replace:  
```python
sender_email = "your-email@gmail.com"
password = "your-password"
```
⚠ **For security, use an App Password instead of your real password**  

3️⃣ **Prepare your files**  
- Add recipient emails in `mail.txt` (one per line)  
- Write your email body in `letter.txt`  
- Place your `resume.pdf` in the same directory  

4️⃣ **Run the script**  
```sh
python send.py
```

✅ The script will send emails and display success or failure messages.  

---

## ⚠ Important Notes  
- If you're using **Gmail**, enable [App Passwords](https://myaccount.google.com/apppasswords) instead of using your real password.  
- Ensure your email provider allows SMTP access.  
- Don't share your credentials in public repositories!  

---

## 📜 License  
This project is licensed under the MIT License.  
