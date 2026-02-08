from supabase import create_client
import re
import supabase
url = "https://koabmxqfnuejulwbscng.supabase.co"
key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
supabase = create_client(url, key)
# print("Connected successfully in check using email")


# def check_student(email="", roll_no=""):
#     if not email and not roll_no:
#         return None

#     value = email if email else roll_no

#     res = supabase.table("Student_Data").select("Password").or(f"Email_Id.eq.{value},Roll_No.eq.{value}").execute()

#     if not res.data:
#         return None

#     print("Student found:", res.data)
#     return res.data

def check_input(value):
    if re.fullmatch(r"[0-9]{10}", value):
        return "mobile"
    elif re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value):
        return "email"
    else:
        return "invalid"


def check_student(value):
    input_type = check_input(value)

    if input_type == "email":
        res = (
            supabase
            .table("Student_Data")
            .select("Password")
            .eq("Email_Id", value)
            .execute()
        )
        print("Student found by email:", res.data)
        return res.data

    elif input_type == "mobile":
        res = (
            supabase
            .table("Student_Data")
            .select("Password")
            .eq("Phone_no", int(value))  
            .execute()
        )
        
        print("Student found by roll no:", res.data)
        return res.data

    else:
        print("Invalid input")
        return None
























def check_teacher(value):
    input_type = check_input(value)

    if input_type == "email":
        res = (
            supabase
            .table("Teacher_Data")
            .select("Password")
            .eq("Email_Id", value)
            .execute()
        )
        print("teacher found by email:", res.data)
        return res.data

    elif input_type == "mobile":
        res = (
            supabase
            .table("Teacher_Data")
            .select("Password")
            .eq("Phone_no", int(value))  
            .execute()
        )
        
        print("teacher found by roll no:", res.data)
        return res.data

    else:
        print("Invalid input")
        return None






























def check_head(value):
    input_type = check_input(value)

    if input_type == "email":
        res = (
            supabase
            .table("Head_Data")
            .select("Password")
            .eq("Email_Id", value)
            .execute()
        )
        print("head found by email:", res.data)
        return res.data

    elif input_type == "mobile":
        res = (
            supabase
            .table("Head_Data")
            .select("Password")
            .eq("Phone_no", int(value))  
            .execute()
        )
        
        print("head found by roll no:", res.data)
        return res.data

    else:
        print("Invalid input")
        return None


print("check student ",check_student("samirsx38@gmail.com"))

# print(check_input("8799673722"))