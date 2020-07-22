import tkinter as tk
from tkinter import RIGHT, CENTER, TOP
import sqlite3
import sys
import datetime
from sqlite3 import Error
from home2 import *
from globalDict import *
from login import *

class createAccount2:
    def __init__(self, fname, mname, lname, dob, num, window):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.dob = dob
        self.num = num
        self.age = "2" ## must chnge later

        # create the window
        self.window = window


        title = tk.Label(master = window, text = "\nCreate new account\n")
        title.configure(font=("Lucida Console", 15, "bold"))
        title.pack()


        ques = tk.Label(master = window, text="Enter security question")
        ques.configure(font=("Lucida Console", 13))
        ques.pack()
        q_entry = tk.Entry(master = window)

        q_entry.insert(0,"Security question")
        q_entry.pack()
        space = tk.Label(master = window, text="\n")
        space.pack()


        ans = tk.Label(master = window, text="Answer")
        ans.configure(font=("Lucida Console", 13))
        ans.pack()
        ans_entry = tk.Entry(master = window)

        ans_entry.insert(0,"")
        ans_entry.pack()
        space = tk.Label(master = window, text="\n")
        space.pack()

        med = tk.Label(master=window, text="Medical condition")
        med.configure(font=("Lucida Console", 13))
        med.pack()
        med_entry = tk.Entry(master=window)

        med_entry.insert(0, "Allergy etc.")
        med_entry.pack()
        space = tk.Label(master=window, text="\n")
        space.pack()


        email = tk.Label(master = window, text="Email")
        email.configure(font=("Lucida Console", 13))
        email.pack()
        email_entry = tk.Entry(master = window)

        email_entry.insert(0,"email@example.com")
        email_entry.pack()
        space = tk.Label(master = window, text="\n")
        space.pack()


        passW = tk.Label(master = window, text="Choose password")
        passW.configure(font=("Lucida Console", 13))
        passW.pack()
        pass_entry = tk.Entry(master = window, show= "*")
        pass_entry.insert(0,"")
        pass_entry.pack()
        #space = tk.Label(master = window, text="\n")
        #space.pack()

        def createAcc():
            try:
                conn = sqlite3.connect('C:\\Users\\HimelSaha\\Documents\\PyCharm Projects\\Hospital app\\record.db')
                print(conn)
                print("::Database connected successfully::")
            except Error as e:
                print(e)
                print("::Failed to connect to the database::")
                sys.exit(1)

            try:
                conn.execute(
                    'CREATE table record(id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, middle TEXT, last TEXT, '
                    'bday DATE, number NUMERIC, question TEXT, ans TEXT, email TEXT, pass TEXT)')
                print("::Table created successfully::", end="\n\n")
            except:
                print("::Table already exists::", end="\n\n")

            checkmail = None
            try:
                email_check = conn.execute(f"SELECT email from record WHERE email = '{email_entry.get()}'").fetchall()
                for i in email_check:
                    checkmail = i[0]
                    break
            except Error as e:
                print(e)

            if checkmail == email_entry.get():
                emailexists = tk.Label(master=window, text="Email already exists")
                emailexists.configure(font=("Lucida Console", 8))
                emailexists.pack()
                return 0

            try:
                conn.execute(
                    'CREATE table record(id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, middle TEXT, last TEXT, '
                    'bday DATE, age NUMERIC, number NUMERIC, question TEXT, ans TEXT, email TEXT, pass TEXT)')
                print("::Table created successfully::", end="\n\n")
            except:
                print("::Table already exists::", end="\n\n")
            date_obj = datetime.datetime.strptime(self.dob, '%Y-%m-%d').date()
            entries = (
            self.fname, self.mname, self.lname, date_obj, int(self.num), q_entry.get(), ans_entry.get(),
            email_entry.get(), pass_entry.get())

            conn.execute(
                "INSERT INTO record(first, middle, last, bday, number, question, ans, email, pass) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                entries)
            conn.commit()
            conn.close()
            window.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.window)  # close the first window
            toplevel.geometry("853x480")
            homepage(email_entry.get(), toplevel)

            d[f"{email}"]= Patient(self.fname + " " + self.mname + " " + self.lname, self.dob, med_entry.get(), email_entry.get())

        b1 = tk.Button(master=window,text = "Create account", command=createAcc, bg = "purple")
        b1.pack()


        #window.geometry("853x480")
        #window.mainloop()