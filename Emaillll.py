import email
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








def send_complaint_email_to_TO_person(
    to_email,
	complaint_text_short,
	complaint_to_name,
	my_role,
	my_name,
	my_contact,
	my_id,
	against_role,
	against_name,
	against_contact_or_id,
	complaint_text
):
     

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(
        "karavadarasamir92@gmail.com",
        "pfni yacj uvmb jqya"
    )
    

    message = f"""Subject: Complaint Regarding {complaint_text_short}

Dear {complaint_to_name},

A complaint has been formally submitted. Details are as follows:

--- Complainant Details ---
Role   : {my_role}
Name   : {my_name}
Contact: {my_contact}
ID     : {my_id}

--- Complaint Against ---
Role       : {against_role}
Name       : {against_name}
Contact/ID : {against_contact_or_id}

--- Complaint Details ---
{complaint_text}

Regards,
{my_name}
{my_contact}
"""
    
    server.sendmail(
        "karavadarasamir92@gmail.com",
        to_email,
        message
    )

    server.quit()
    print("Email sent successfully for complaint to TO person")




# send_complaint_email_against("samirsx38@gmail.com", "hello" , "samir karavadara" , 741258963)
# send_complaint_email_my("samirsx38@gmail.com" ,  "hello" , "samir karavadara" , 741258963)

# send_complaint_email_to_TO_person(
#     "rajputmihir2006@gmail.com",
#     "Test Complaint",
#     "John Doe",
#     "Manager",
#     "Samir Karavadara",
#     "9876543210",
#     "EMP001",
#     "Employee",
#     "Alice Smith",
#     "EMP002",
#     "The employee was found to be unprofessional and disrespectful during a meeting."
# )