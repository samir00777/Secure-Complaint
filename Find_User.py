from supabase import create_client

def FIND_HEAD_IN_SUPABASE(id):
    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
    supabase = create_client(url, key)
    print("Connected successfully")

    res = supabase.table("Head_Data").select("*").eq("Head_Id", id).execute()

    if res == None or len(res.data) == 0:
        print("No data found for Head_Id ")
    else:
        print("User found", res.data)

    