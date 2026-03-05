from supabase import create_client


def heandle_complaint(table):
        
    url = "https://koabmxqfnuejulwbscng.supabase.co"
    key =  "--your api key--"
    supabase = create_client(url, key)

    supabase = create_client(url, key)


    res = supabase.table(table).select("id").order("id").limit(1).execute()

    if res.data:
        first_id = res.data[0]["id"]


        supabase.table(table).delete().eq("id", first_id).execute()
        print("First row deleted")
    else:
        print("Table is empty")

    new_res = supabase.table(table).select("*").execute()

    print("next complaint is : ------------->>>>>> ", new_res.data[0]["Complaint"])




# heandle_complaint("Student_Data")