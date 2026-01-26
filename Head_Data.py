from supabase import create_client
import httpx


def INSERT_HEAD_DATA_IN_SUPABASE(Head_id, Name, Phone_no, Email, password):
    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
    supabase = create_client(url, key)

    supabase = create_client(url, key)
    print("Connected successfully")

    data = {
        "Head_Id": Head_id,
        "Name": Name,
        "Phone": Phone_no,
        "Email": Email,
        "Password": password
    }


    supabase.table("Head_Data").insert(data).execute()
