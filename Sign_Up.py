from flask import Flask, render_template, request , send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("Sign_Up.html")

@app.route("/signup", methods=["POST"])
def signup():
    role = request.form.get("role")
    method = request.form.get("method")

    print("Role:", role)
    print("Method:", method)

    if role == "student":
        password = request.form.get("password")
        if method == "phone":
            phone = request.form.get("phone")
            print(phone , password)
        elif method == "email":
            email = request.form.get("email")
            print(email , password)
        

    elif role == "teacher":
        password = request.form.get("password")
        if method == "phone":
            phone = request.form.get("phone")
            print(phone , password)
        elif method == "email":
            email = request.form.get("email")
            print(email , password)
    elif role == "head":
        password = request.form.get("password")
        if method == "phone":
            phone = request.form.get("phone")
            print(phone , password)
        elif method == "email":
            email = request.form.get("email")
            print(email , password)
    else:
        print("Unknown role")



    return "Data received successfully"

if __name__ == "__main__":
    app.run(debug=True)

