from supabase import create_client
import httpx


def INSERT_HEAD_DATA_IN_SUPABASE(Head_id, Name, Phone_no, Email, password):
    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "--your api key--"
    supabase = create_client(url, key)

    supabase = create_client(url, key)
    print("Connected successfully")

    data = {
        "Head_Id": Head_id,
        "Name": Name,
        "Email_Id": Email,
        "Phone_no": Phone_no,
        "Password": password
    }


    supabase.table("Head_Data").insert(data).execute()
