# from supabase import create_client
# import httpx

# url = "https://koabmxqfnuejulwbscng.supabase.co"
# key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
# supabase = create_client(url, key)
# print("Connected successfully")

# res = supabase.table("Head_Data").select("*").eq("Head_Id", 101).execute()

# print(res.data)

# import Sign_Up
# Sign_Up.home()

from Sign_Up import app as aa


if __name__ == "__main__":
    aa.run(debug=True)
