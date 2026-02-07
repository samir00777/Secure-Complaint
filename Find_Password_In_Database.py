# "Email_Id"
# Phone_no
from supabase import create_client
url = "https://koabmxqfnuejulwbscng.supabase.co"
key =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtvYWJteHFmbnVlanVsd2JzY25nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcyNzg1MDAsImV4cCI6MjA4Mjg1NDUwMH0.sGhBrRGwlcxK9JWT4FOGnAbIGNa_3xve4ISOE1-hZWM"
   

# def FIND_HEAD_IN_SUPABASE_(thru , id):

    
#     supabase = create_client(url, key)
#     print("Connected successfully")

#     res = supabase.table("Head_Data").select("*").eq(thru, id).execute()

#     a = res.data
#     return a[0].get("Password")



# def FIND_TEACHER_IN_SUPABASE(thru , id):
#     supabase = create_client(url, key)
#     print("Connected successfully")

#     x = supabase.table("Teacher_Data").select("*").eq(thru, id).execute()
#     a = x.data
#     return a[0].get("Password")




# def FIND_STUDENT_IN_SUPABASE(thru , id):


#     supabase = create_client(url, key)
#     print("Connected successfully")


#     x = supabase.table("Student_Data").select("*").eq(thru, id).execute()
#     a = x.data

#     return a[0].get("Password")


# print(FIND_STUDENT_IN_SUPABASE("Email_Id", "Samir@123.com"))
# print(FIND_STUDENT_IN_SUPABASE("Phone_no", "8799673722"))








# from supabase import create_client

supabase = create_client(url, key)


def FIND_STUDENT_IN_SUPABASE(thru, value):


    res = supabase.table("Student_Data").select("Password").eq(thru, value).execute()

    if not res.data:
        return None

    return res.data[0]["Password"]


def FIND_TEACHER_IN_SUPABASE(thru, value):


    res = supabase.table("Teacher_Data").select("Password").eq(thru, value).execute()

    if not res.data:
        return None

    return res.data[0]["Password"]


def FIND_HEAD_IN_SUPABASE(thru, value):


    res = supabase.table("Head_Data").select("Password").eq(thru, value).execute()

    if not res.data:
        return None

    return res.data[0]["Password"]

# x= f'''
# {FIND_STUDENT_IN_SUPABASE("Email_Id", "Samir@123.com")}
# {FIND_STUDENT_IN_SUPABASE("Phone_no", "8799673722")}'''

# print(x)