import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(
    "karavadarasamir92@gmail.com",
    "pfni yacj uvmb jqya"
)

def send_email_using_smtplib(email, new_otp):
    

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



def send_complaint_email(email, complaint_details , name , mobile):
    message = f'''Dear Sir/Madam,

I would like to raise a complaint regarding 

**{complaint_details}**.

Sender Details:
Name: {name}
Email: {email}
Mobile: {mobile}

Thank you.

'''