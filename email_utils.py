import random
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("EMAIL_PASSWORD")


# -------------------------------
# Generate OTP
# -------------------------------
def generate_otp():
    return str(random.randint(100000, 999999))


# -------------------------------
# Send OTP
# -------------------------------
def send_otp(receiver_email, otp):
    try:
        subject = "Employee Wellness Management - Password Reset OTP"

        body = f"""
Hello,

Your OTP for resetting your password is:

{otp}

This OTP is valid for 5 minutes.

Thank You
Employee Wellness Management
"""

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(
            SENDER_EMAIL,
            receiver_email,
            msg.as_string()
        )
        server.quit()

        return True

    except Exception as e:
        print("Email Error:", e)
        return False