# import mysql.connector

# # values coming from frontend
# sid = 1
# username = "Samir"
# roll = 12
# marks = 85
# phone_no = 9876543210
# Email = "hello"

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="python"
# )

# print("Connected!")

# cursor = conn.cursor()

# query = """
# INSERT INTO many_try (id, name, roll, marks, phone_no)
# VALUES (%s, %s, %s, %s, %s , %s)
# """

# cursor.execute(query, (sid, username, roll, marks, phone_no , Email))
# conn.commit()

# print("Data inserted successfully")

# conn.close()

import mysql.connector
def str(sid , username , Roll_No , marks , Phone_no , Email):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python"
        )

        # cursor is used to execute SQL queries 
        cursor = conn.cursor()

        # is not write a %s then it is a very unsafe
        # if i write direct value in query using f string then it is unsafe from SQL Injection attack
        # if some error are generate then  value are direct deleted 
        query =  """
                    INSERT INTO info
                    (id , name, roll, marks, phone_no , Email)
                    VALUES (%s , %s , %s , %s , %s , %s)
                    """
        cursor.execute(query, (sid , username , Roll_No , marks , Phone_no , Email))

        # save data in data base 
        # whithout this data was not save in server
        conn.commit()

        # closed both connection with a data base
        # it is a important for a perfomance 
        cursor.close()
        conn.close()

        # send a massge from web
        return f"Hello {username}, \nyour data is {sid , Roll_No , marks , Phone_no , Email}\n\n saved successfully!"

    except mysql.connector.Error as e:
        return f"Database Error: {e}"
