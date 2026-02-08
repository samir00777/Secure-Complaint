# from flask import Flask, request, send_file,redirect,url_for
# Flask --> help for create a webpage
# request --> read data for html
# send_file -->send python file to browser
# import Emaillll
# import connect_with_storage

# app = Flask(__name__)  # create a flask application
# __name__ tells Flask this file is the main app


# ---------------- HOME PAGE ----------------
# @app.route('/')  #When user opens http://127.0.0.1:5000/, this runs
# def home():
    # return send_file('index.html')  # Sends index.html file to browser
# def login():
#     return send_file('login.html')


# ---------------- FORM SUBMIT ----------------
# @app.route('/submit', methods=[ 'POST'])
# URL /submit
# Accepts POST request only
# Form action must be /submit

# def submit():
    # read username from web page
    # and .get mathod is avoid if it is null
    # default store a string

    
    # Returned_by_email = Emaillll.send_email_using_smtplib(Email)


    # return  redirect(url_for('http://127.0.0.1:5000/'))
    # same page are closed and new page are loded 
    # url_for is   auto update page

    # name = request.form['option']
    # print(name)
    # return redirect(url_for('home'))

    


# ---------------- RUN server ----------------
# if __name__ == "__main__":
    # start web server
    # if any error then shows it
    # app.run(debug=True)


# -----------------------------------------------------------------------------------------------------------------------------------------------------************************************************************************************

# 'http://127.0.0.1:5000/'
import random
from flask import Flask, request, send_file, redirect, url_for
import Find_Password_In_Database as find_user
import Emaillll as email_module
import Student_data as student_module
import Teacher_Data as teacher_module
import Head_Data as head_module
import Check_User_For_CMP as check_user



email_for_otp = ""
otp_generated = 0


app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')



@app.route('/submit', methods=['POST'])
def submit():

    ls_option = request.form['LS_option'].lower()
    option = request.form['option'].lower()
    print(option , ls_option)

    if ls_option == 'login':
        if option == 'head':
            return send_file('Front_End_For_Head.html')
        elif option == 'teacher':
            return send_file('Front_End_For_Teacher.html')
        elif option == 'student':
            return send_file('Front_End_For_Student.html')
        else:
            return redirect(url_for('home'))
    elif ls_option == 'signup': 
        # check user found or not
        # find_user.FIND_HEAD_IN_SUPABASE(option)
        # aagad kaam chalu che
        return send_file('Sign_Up.html')




@app.route("/student_submit", methods=['POST'])
def student_submit():
    roll_no = request.form.get('Roll_No')
    enrollment_no = request.form.get('Enrollment_No')
    name = request.form.get('Name')
    email = request.form.get('Email_Id')
    phone = request.form.get('Phone_no')
    password = request.form.get('password')


    print("-------student data-------")
    print(roll_no, enrollment_no, name, email, phone, password)

    student_module.INSERT_STUDENT_DATA_IN_SUPABASE(roll_no, enrollment_no, name, email, phone, password)

    return redirect(url_for('home'))


# ---------------- TEACHER FORM ----------------
@app.route('/teacher_submit', methods=['POST'])
def teacher_submit():
    
    Teacher_id = request.form.get('Teacher_Id')
    Name = request.form.get('Name')
    Phone_no = request.form.get('Phone_no')
    email = request.form.get('Email_Id')
    password = request.form.get('password')


    print("-------teacher data-------")
    print(Teacher_id, Name, Phone_no, email, password)

    teacher_module.INSERT_TEACHER_DATA_IN_SUPABASE(Teacher_id, Name, Phone_no, email, password)

    return redirect(url_for('home'))


# ---------------- HEAD FORM ----------------
@app.route('/head_submit', methods=['POST'])
def head_submit():
    
    Head_id = request.form.get('Head_Id')
    Name = request.form.get('Name')
    Phone_no = request.form.get('Phone_no')
    email = request.form.get('Email_Id')
    password = request.form.get('password')
 
    print("-------head data-------")
    print(Head_id, Name, Phone_no, email, password)

    head_module.INSERT_HEAD_DATA_IN_SUPABASE(Head_id, Name, Phone_no, email, password)

    return redirect(url_for('home'))




# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# ---------------- Sign Up ----------------
@app.route("/signup", methods=["POST"])
def signup():

    global email_for_otp
    global otp_generated
    role = request.form.get("role")
    method = request.form.get("method")
    otp_generated = random.randint(100000, 999999)

    
    print("Role:", role)
    print("Method:", method)

    # return send_file("Otp_Frount_End.html")



















    if role == "student":


        if method == "phone":

            phone = int(request.form.get("phone"))

            received_password = request.form.get("password_for_phone")

            find_password = find_user.FIND_STUDENT_IN_SUPABASE("Phone_no" , phone)
            print("Received Password:", received_password)
            print("find Password:", find_password)

            if received_password == find_password:
                return send_file("Complaint.html")
            
            elif received_password is None:
                return "User not found"
            
            else:
                return "Incorrect Password"

        elif method == "email":


            email_for_otp = request.form.get("email")
            email_module.send_email_using_smtplib(email_for_otp, otp_generated)


            received_password = request.form.get("password_for_email")
            find_password = find_user.FIND_STUDENT_IN_SUPABASE("Email_Id" , email_for_otp)


            print("Received Password:", received_password)
            print("find Password:", find_password)
            print("email_for_otp:", email_for_otp)


            if find_password is None:
                return "User not found"
            
            elif received_password == find_password:
                return send_file("Otp_Frount_End.html")

            else:
                return "Incorrect Password"

        


        
























    elif role == "teacher":

        if method == "phone":
            phone = int(request.form.get("phone"))

            received_password = request.form.get("password_for_phone")
            find_password = find_user.FIND_TEACHER_IN_SUPABASE("Phone_no" , phone)
            print("Received Password:", received_password)
            print("find Password:", find_password)

            if received_password == find_password:
                return send_file("complaint.html")
            
            elif received_password is None:
                return "User not found"
            
            else:
                return "Incorrect Password"


        elif method == "email":
            email_for_otp = request.form.get("email")

            email_module.send_email_using_smtplib(email_for_otp, otp_generated)

            received_password = request.form.get("password_for_email")
            find_password = find_user.FIND_TEACHER_IN_SUPABASE("Email_Id" , email_for_otp)

            print("Received Password:", received_password)
            print("find Password:", find_password)


            if received_password == find_password:
                return send_file("Otp_Frount_End.html")
            
            elif received_password is None:
                return "User not found"
            
            else:
                return "Incorrect Password"

            
        

































    elif role == "head":

        if method == "phone":


            phone = int(request.form.get("phone"))
            print("Phone:", phone)


            received_password = request.form.get("password_for_phone")
            find_password = find_user.FIND_HEAD_IN_SUPABASE("Phone_no" , phone)
            print("Received Password:", received_password)
            print("find Password:", find_password)

            if received_password == find_password:
                return send_file("complaint.html")
            
            elif received_password is None:
                return "User not found"
            
            else:
                return "Incorrect Password"


        elif method == "email":
            email_for_otp = request.form.get("email")

            email_module.send_email_using_smtplib(email_for_otp, otp_generated)

            received_password = request.form.get("password_for_email")
            find_password = find_user.FIND_HEAD_IN_SUPABASE("Email_Id" , email_for_otp)

            print("Received Password:", received_password)
            print("find Password:", find_password)

            if received_password == find_password:
                return send_file("Otp_Frount_End.html")
            
            elif received_password is None:
                return "User not found"
            
            else:
                return "Incorrect Password"
            
    return "Data received successfully"


# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm


    



@app.route("/signup_otp", methods=["POST"])
def otp_verification():

    print("-------OTP Verification-------")
    global email_for_otp
    global otp_generated

    
    received_otp = request.form.get("otp")

    print("Email:", email_for_otp)
    print("Received OTP:", received_otp)
    print("Generated OTP:", otp_generated)

    



    if str(received_otp) == str(otp_generated):
        return send_file("Complaint.html")
    else:
        return ("Invalid OTP. Please try again.")
    

















# COMPLAINT CODE
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------





# @app.route("/Complaint", methods=["POST"])
# def signup():

@app.route("/submit_complaint", methods=["POST"])
def submit_complaint():

    my_role = request.form.get("my_role").lower()
    against_role = request.form.get("against_role").lower()

    # data = {
    #     "my_role": my_role,
    #     "against_role": against_role,
    #     "student_name": request.form.get("student_name"),
    #     "student_contact": request.form.get("student_contact"),
    #     "student_roll": request.form.get("student_roll"),
    #     "teacher_name": request.form.get("teacher_name"),
    #     "teacher_contact": request.form.get("teacher_contact"),
    #     "teacher_id": request.form.get("teacher_id"),
    #     "head_name": request.form.get("head_name"),
    #     "head_contact": request.form.get("head_contact"),
    #     "head_id": request.form.get("head_id"),
    #     "against_student_name": request.form.get("against_student_name"),
    #     "against_student_roll": request.form.get("against_student_roll"),
    #     "complaint_student": request.form.get("complaint_student"),
    #     "against_teacher_name": request.form.get("against_teacher_name"),
    #     "against_teacher_contact": request.form.get("against_teacher_contact"),
    #     "complaint_teacher": request.form.get("complaint_teacher"),
    #     "against_head_name": request.form.get("against_head_name"),
    #     "against_head_contact": request.form.get("against_head_contact"),
    #     "complaint_head": request.form.get("complaint_head")
    # }

    # print(data)



    my_data = {}
    if my_role == "student":
        my_data["name"] = request.form.get("my_student_full_name")
        my_data["contact"] = request.form.get("my_student_contact_info")
        my_data["id"] = request.form.get("my_student_roll_number")

    elif my_role == "teacher":
        my_data["name"] = request.form.get("my_teacher_full_name")
        my_data["contact"] = request.form.get("my_teacher_contact_info")
        my_data["id"] = request.form.get("my_teacher_id")

    elif my_role == "head":
        my_data["name"] = request.form.get("my_head_full_name")
        my_data["contact"] = request.form.get("my_head_contact_info")
        my_data["id"] = request.form.get("my_head_id")

    against_data = {}
    if against_role == "student":
        against_data["name"] = request.form.get("against_student_full_name")
        against_data["id"] = request.form.get("against_student_roll_number")
        against_data["complaint"] = request.form.get("against_student_complaint_text")

    elif against_role == "teacher":
        against_data["name"] = request.form.get("against_teacher_full_name")
        against_data["contact"] = request.form.get("against_teacher_contact_info")
        against_data["complaint"] = request.form.get("against_teacher_complaint_text")

    elif against_role == "head":
        against_data["name"] = request.form.get("against_head_full_name")
        against_data["contact"] = request.form.get("against_head_contact_info")
        against_data["complaint"] = request.form.get("against_head_complaint_text")

    print("my role --> ",my_role)
    print("against role --> ",against_role)
    print("my data --> ",my_data)
    print("against data --> ",against_data)


    



    if my_role == "student" and against_role == "student":
        pass
    elif my_role == "teacher" and against_role == "student":
        pass
    elif my_role == "head" and against_role == "student":
        pass
    elif my_role == "student" and against_role == "teacher":
        pass
    elif my_role == "teacher" and against_role == "teacher":
        pass
    elif my_role == "head" and against_role == "teacher":
        pass
    elif my_role == "student" and against_role == "head":
        pass
    elif my_role == "teacher" and against_role == "head":
        pass
    elif my_role == "head" and against_role == "head":
        pass



    return "Complaint raised Successfully"




    
if __name__ == "__main__":
    app.run(debug=True)



