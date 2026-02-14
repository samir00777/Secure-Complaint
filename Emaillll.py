from email.mime import message
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
    print("email sent successfully for OTP verification")



def send_complaint_email_against(mobile,  complaint_details , name , email):


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(
        "karavadarasamir92@gmail.com",
        "pfni yacj uvmb jqya"
    )
    

    message = f'''Dear Sir/Madam,

    I would like to raise a complaint regarding 

    **{complaint_details}**.

    Sender Details:
    Name: {name}
    Email: {email}
    Mobile: {mobile}

    Thank you.

    '''

    server.sendmail(
        "karavadarasamir92@gmail.com",
        email,
        message
    )

    server.quit()
    print("Email sent successfully for complaint against someone")



def send_complaint_email_my(mobile,  complaint_details , name , email):


    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(
        "karavadarasamir92@gmail.com",
        "pfni yacj uvmb jqya"
    )
    

    message = f'''Dear {name},

This is to inform you about a complaint regarding **{complaint_details}**.
Kindly look into the matter at your earliest convenience.

Regards,
{name}
{mobile}

'''
    server.sendmail(
        "karavadarasamir92@gmail.com",
        email,
        message
    )

    server.quit()
    print("Email sent successfully for complaint to my self")


# send_complaint_email_against("samirsx38@gmail.com", "hello" , "samir karavadara" , 741258963)
# send_complaint_email_my("samirsx38@gmail.com" ,  "hello" , "samir karavadara" , 741258963)