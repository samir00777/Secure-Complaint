import re

def check_input(value):
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    phone_regex = r'^\d{10}$'

    if re.match(email_regex, value):
        return "Email"
    elif re.match(phone_regex, value):
        return "Phone"
    else:
        return "Invalid"

# Examples
print(check_input("samir@gmail.com"))
print(check_input("9876543210"))