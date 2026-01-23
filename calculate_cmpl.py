import Emaillll as email_module
import Student_data as student_module
import Teacher_Data as teacher_module
import Head_Data as head_module



def SEND_MAIL(mail):
    print(email_module.send_email_using_smtplib(mail))



# --------------------STUDENT inseert & mail sending--------------------
def INSERT_STUDENT(data):
    student_module.INSERT_STUDENT_DATA_IN_SUPABASE(data)
    SEND_MAIL(data)



#------------------------TEACHER insert & mail sending--------------------
def INSERT_TEACHER(data):
    teacher_module.INSERT_TEACHER_DATA_IN_SUPABASE(data)
    SEND_MAIL(data)


# ------------------------HEAD insert & mail sending--------------------
def INSERT_HEAD(data):
    head_module.INSERT_HEAD_DATA_IN_SUPABASE(data)
    SEND_MAIL(data)