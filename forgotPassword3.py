import tkinter as tk
import sqlite3
from sqlite3 import *
import sys

class forgotPassword3():
    def __init__(self, email,windows):
        # create the window
        #window = tk.Tk()
       
        self.windows = windows
        #create a lable, won't show up to the window until the next line
        title = tk.Label(master=windows,text = "\nReset password\n")
        title.configure(font=("Lucida Console", 20, "bold"))
        title.pack()

        # security question
        sq = tk.Label(master=windows,text="\nEnter new password")
        sq.configure(font=("Lucida Console", 15))
        sq.pack()
        space = tk.Label(master=windows,text="\n")
        space.pack()
        pWord = tk.Entry(master=windows)
        pWord.insert(0,"Enter new pass")
        pWord.pack()

        def change():
            newPass = pWord.get()
            try:
                conn = sqlite3.connect('C:\\Users\\HimelSaha\\Documents\\PyCharm Projects\\Hospital app\\record.db')
                print(conn)
                print("::Database connected successfully::")
            except Error as e:
                print(e)
                print("::Failed to connect to the database::")
                sys.exit(1)
            try:
                conn.execute(f"UPDATE record SET pass = '{newPass}' WHERE email = '{email}'")

            except Error as e:
                print(e)

            try:
                ansFound = conn.execute(f"SELECT pass from record WHERE email = '{email}'").fetchall()
                for i in ansFound:
                    # lista_tags.append(i)
                    passfromDB = i[0]
                    conn.commit()
                    conn.close()
                    break
            except Error as e:
                print(e)
            if passfromDB == newPass:
                print("yess")
                success = tk.Label(master=windows, text="Password changed succesfully")
                success.pack()
            else:
                print("nno")

        space = tk.Label(master=windows,text="\n")
        space.pack()
        space = tk.Label(master=windows,text="\n")
        space.pack()
        b1 = tk.Button(master=windows,text = "Change password", command=change)
        b1.pack()
        space = tk.Label(master=windows,text="\n")
        space.pack()
