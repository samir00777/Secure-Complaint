# # from supabase import create_client
# # import httpx

# # url = "https://koabmxqfnuejulwbscng.supabase.co"
# # key =  "--your api key--"
# # supabase = create_client(url, key)
# # print("Connected successfully")

# # res = supabase.table("Head_Data").select("*").eq("Head_Id", 101).execute()

# # print(res.data)

# # import Sign_Up
# # Sign_Up.home()

# # from Sign_Up import app as aa


# # if __name__ == "__main__":
# #     aa.run(debug=True)


# # x = "hello"

# # def aa():
# #     global x
# #     print(x)
# #     x = "hi"

# # def bb():
# #     x = "hello world"
# #     print(x)

# # aa()
# # bb()


# # import Emaillll as e
# # e.send_email_using_smtplib("--your email--", 123456)



# # if True:
# #     x = "hello"

# # print(x)




# print('''Dear Sir/Madam,

#     I would like to raise a complaint regarding

#     **11111111111111**.

#     Sender Details:
#     Name: Samir Karavadara2
#     Email: --your email--
#     Mobile: Phone: 8799673722
# Email: --your email--

#     Thank you.
# ''' == '''Dear Sir/Madam,

#     I would like to raise a complaint regarding

#     **11111111111111**.

#     Sender Details:
#     Name: samir-2
#     Email: --your email--

#     Mobile: Phone: 1234567890
# Email: --your email--

#     Thank you.
# ''')























import tkinter as tk

root = tk.Tk()
root.title("Two Partition Layout")
root.geometry("800x400")

left_frame = tk.Frame(root, bg="#f5f5f5", width=400)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(root, bg="#e0e0e0", width=400)
right_frame.pack(side="right", fill="both", expand=True)

tk.Label(left_frame, text="Left Partition", font=("Arial", 14)).pack(pady=20)
tk.Label(right_frame, text="Right Partition", font=("Arial", 14)).pack(pady=20)

root.mainloop()
