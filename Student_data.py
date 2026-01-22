from supabase import create_client
import httpx

url = "https://koabmxqfnuejulwbscng.supabase.co"
key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
supabase = create_client(url, key)

supabase = create_client(url, key)
print("Connected successfully")

data = {
    "Roll_No": 12,
    "Enrollment_No": 123456789012,
    "Name": "Samir Karavadara",
    "Email_Id": "samir@gmail.com",
    "Phone_no": 9876543210,
    "Complaint": "Water facility is not working properly"
}

supabase.table("Student_Data").insert(data).execute()