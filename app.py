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









from flask import Flask, request, send_file, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    option = request.form['option']
    print(option)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
