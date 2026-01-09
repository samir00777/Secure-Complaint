from supabase import create_client
import httpx


print("Connected successfully")

data = {
    "Roll_No": 12,
    "Enrollment_No": 123456789012,
    "Name": "Samir Karavadara",
    "Email_Id": "samir@gmail.com",
    "Phone_no": 9876543210,
    "Complaint": "Water facility is not working properly"
}

# res = supabase.table("Student_Data").insert(data).execute()
# print(res.data, "<-----------")