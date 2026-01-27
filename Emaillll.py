import smtplib

def send_email_using_smtplib(email):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("karavadarasamir92@gmail.com", "pfni yacj uvmb jqya")

    server.sendmail(
        "karavadarasamir92@gmail.com",
        f"{email}",  # samirsx38@gmail.com
        '''Subject: Test Mail\n\nEmail sent using Python 
            hello i am samir i talking about hardwork '''
    )

    server.quit()
    return "Email sent successfully"


# print(send_email_using_smtplib("dakshra0906@gmail.com"))