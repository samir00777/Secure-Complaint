from supabase import create_client
import httpx

def insert_complaint(
    my_role, my_name, my_contact,
    against_role, against_name, against_contact,
    to_role, to_name, to_contact , complaint_text):



    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "--your api key--"
    supabase = create_client(url, key)

    supabase = create_client(url, key)
    # print("Connected successfully")

    data = {
        "My_Role": my_role,
        "My_Name": my_name,
        "My_Contect": my_contact,
        "Against_Role": against_role,
        "Against_Name": against_name,
        "Against_Contect": against_contact,
        "To_Role": to_role, 
        "To_Name": to_name,
        "To_Contect": to_contact,
        "Complaint": complaint_text
    }


    supabase.table("Complaint_Data").insert(data).execute()



# my_role = "student"
# my_name = "Samir"
# my_contact = "9999999999"

# against_role = "teacher"
# against_name = "Mr. Patel"
# against_contact = "8888888888"

# to_role = "admin"
# to_name = "Principal"
# to_contact = "7777777777"

# insert_complaint(
#     my_role, my_name, my_contact,
#     against_role, against_name, against_contact,
#     to_role, to_name, to_contact
# )