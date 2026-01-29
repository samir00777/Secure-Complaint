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
import Find_User as find_user
import Emaillll as email_module
import Student_data as student_module
import Teacher_Data as teacher_module
import Head_Data as head_module



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

    # print("-------head data-------")
    # print(Head_id, Name, Phone_no, email, password)

    head_module.INSERT_HEAD_DATA_IN_SUPABASE(Head_id, Name, Phone_no, email, password)

    return redirect(url_for('home'))





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
        received_password = request.form.get("password")
        find_password = find_user.FIND_STUDENT_IN_SUPABASE(role, method, request.form)
        print("Received Password:", received_password)
        print("find Password:", find_password)


        
        
    

        if method == "phone":
            phone = request.form.get("phone")
            print(phone , password)


        elif method == "email":
            email_for_otp = request.form.get("email")
            print(email_for_otp , password)
            email_module.send_email_using_smtplib(email_for_otp, otp_generated)
            return send_file("Otp_Frount_End.html")
        

    elif role == "teacher":
        password = request.form.get("password")

        if method == "phone":
            phone = request.form.get("phone")
            print(phone , password)


        elif method == "email":
            email_for_otp = request.form.get("email")
            print(email_for_otp , password)
            email_module.send_email_using_smtplib(email_for_otp, otp_generated)
            return send_file("Otp_Frount_End.html")
        

    elif role == "head":
        password = request.form.get("password")

        if method == "phone":
            phone = request.form.get("phone")
            print(phone , password)


        elif method == "email":
            email_for_otp = request.form.get("email")
            print(email_for_otp , password)
            email_module.send_email_using_smtplib(email_for_otp, otp_generated)
            return send_file("Otp_Frount_End.html")
            
    return "Data received successfully"


    



@app.route("/signup_otp", methods=["POST"])
def otp_verification():

    print("-------OTP Verification-------")
    global email_for_otp
    global otp_generated
    received_otp = request.form.get("otp")

    print("Email:", email_for_otp)
    print("Received OTP:", received_otp)

    



    if str(received_otp) == str(otp_generated):
        return ("OTP verified successfully")
    else:
        return ("Invalid OTP. Please try again.")
    
if __name__ == "__main__":
    app.run(debug=True)




















# ------------------ new code -------------------------------------------------

