import smtplib


def send_email_using_smtplib(email, new_otp):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(
        "karavadarasamir92@gmail.com",
        "pfni yacj uvmb jqya"
    )

    message = f"""Subject: OTP Verification

Hello,
Thank you for signing up.

Your One-Time Password (OTP) is:
OTP: {new_otp}

Do not share this OTP with anyone.

Regards,
Your App Team
"""

    server.sendmail(
        "karavadarasamir92@gmail.com",
        email,
        message
    )

    server.quit()
    print("Email sent successfully")