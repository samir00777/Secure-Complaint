from supabase import create_client
import httpx

url = "https://koabmxqfnuejulwbscng.supabase.co"
key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
supabase = create_client(url, key)
print("Connected successfully")

data = {
    "Teachers_Id": 1,
    "Name": "Samir Karavadara",
    "Phone_no": "9876543210",
    "Email_Id": "samir@gmail.com",   # <-- FIXED
    "Complaint": "Water facility is not working properly"
}

supabase.table("Teacher_data").insert(data).execute()
