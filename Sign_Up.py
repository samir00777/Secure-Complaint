from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def signup():
    return send_file("Sign_Up.html")

if __name__ == "__main__":
    app.run(debug=True)

def run_signup_app():
    print("Starting Sign Up App...")