from supabase import create_client
import httpx



def INSERT_TEACHER_DATA_IN_SUPABASE(teacher_id, name, phone_no, email_id, password):
    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
    supabase = create_client(url, key)
    print("Connected successfully")

    data = {
        "Teachers_Id": teacher_id,
        "Name": name,
        "Phone_no": phone_no,
        "Email_Id": email_id,
        "Password": password
    }

    supabase.table("Teacher_Data").insert(data).execute()
