from supabase import create_client
import supabase
url = "https://koabmxqfnuejulwbscng.supabase.co"
key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
supabase = create_client(url, key)
print("Connected successfully in check using email")


def check_student(email = "", id = ""):
    res = supabase.table("Student_Data").select("Password").or_(f"Email_Id.eq.{email},Roll_No.eq.{id}").execute()

    if not res.data:
        return None

    print("Student found:", res.data)

def check_teacher():
    pass

def check_head():
    pass


check_student("9724353739")