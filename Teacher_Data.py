from supabase import create_client
import httpx



def INSERT_TEACHER_DATA_IN_SUPABASE(teacher_id, name, phone_no, email_id, password):
    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "--your api key--"
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
