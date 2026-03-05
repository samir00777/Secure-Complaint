from supabase import create_client
import httpx

def INSERT_STUDENT_DATA_IN_SUPABASE(roll_no, enrollment_no, name, email_id, phone_no, password):
    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "--your api key--"
    supabase = create_client(url, key)

    supabase = create_client(url, key)
    print("Connected successfully")

    data = {
        "Roll_No": roll_no,
        "Enrollment_No": enrollment_no,
        "Name": name,
        "Email_Id": email_id,
        "Phone_no": phone_no,
        "Password": password
    }

    supabase.table("Student_Data").insert(data).execute()