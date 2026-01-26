import Emaillll as email_module
import Student_data as student_module
import Teacher_Data as teacher_module
import Head_Data as head_module



def SEND_MAIL(mail):
    print(email_module.send_email_using_smtplib(mail))



# --------------------STUDENT inseert & mail sending--------------------
def INSERT_STUDENT(Roll_no, Enrollment_No, Name, Email_Id, Phone_no, Password):
    student_module.INSERT_STUDENT_DATA_IN_SUPABASE(Roll_no, Enrollment_No, Name, Email_Id, Phone_no, Password)
    SEND_MAIL(Email_Id)



#------------------------TEACHER insert & mail sending--------------------
def INSERT_TEACHER(Teacher_id, Name, Phone_no, Email_Id, Password):
    teacher_module.INSERT_TEACHER_DATA_IN_SUPABASE(Teacher_id, Name, Phone_no, Email_Id, Password)
    SEND_MAIL(Email_Id)


# ------------------------HEAD insert & mail sending--------------------
def INSERT_HEAD(Head_id, Name, Phone_no, Email_Id, Password):
    head_module.INSERT_HEAD_DATA_IN_SUPABASE(Head_id, Name, Phone_no, Email_Id, Password)
    SEND_MAIL(Email_Id)