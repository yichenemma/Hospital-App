from DBConnection import Database
from oldUser import *
import tkinter as tk
import datetime
import sqlite3
import sys
from sqlite3 import Error
from forgotPassword3 import *

class forgotPassword2:
    def __init__(self, email, windows):
        self.email = email
        self.ques = ""
        self.windows = windows
        conn = None
##        # create the window
        #windows = tk.Tk()

        # search security ques
        try:
            conn = sqlite3.connect('C:\\Users\\HimelSaha\\Documents\\PyCharm Projects\\Hospital app\\record.db')
            print(conn)
            print("::Database connected successfully::")
        except Error as e:
                print(e)
                print("::Failed to connect to the database::")
                sys.exit(1)
        try:
            quesFound = conn.execute(f"SELECT question from record WHERE email = '{self.email}'").fetchall()
            for i in quesFound:
                #lista_tags.append(i)
                ques = i[0]
                break
        except Error as e:
            print(e)

        #####################

        #create a lable, won't show up to the window until the nexet line
        title = tk.Label(master=windows,text="\nReset password\n")
        title.configure(font=("Lucida Console", 20, "bold"))
        title.pack()

        # security question
        sq = tk.Label(master=windows,text=ques)
        sq.configure(font=("Lucida Console", 15))
        sq.pack()
        space = tk.Label(master=windows,text="\n")
        space.pack()
        ans = tk.Entry(master=windows,)
        ans.insert(0, "Enter response")
        ans.pack()

        def validate():
            try:
                ansFound = conn.execute(f"SELECT ans from record WHERE question = '{ques}' and email = '{email}'").fetchall()
                for i in ansFound:
                    # lista_tags.append(i)
                    answer = i[0]
                    break

            except Error as e:
                print(e)
            conn.commit()
            
            if answer == ans.get():
                print("RIGHT ANSWER!!!")
               

                windows.withdraw() # to close the window!!
                toplevel = tk.Toplevel(self.windows) # close the first window
                toplevel.geometry("853x480")
                forgotPassword3(email,toplevel)
                

            else:
                print("Wrong answer")
                oops = tk.Label(master=windows, text="Wrong security question answer")
                oops.pack()

        space = tk.Label(master=windows, text="\n")
        space.pack()
        space = tk.Label(master=windows, text="\n")
        space.pack()
        b1 = tk.Button(master=windows, text="Next", command=validate)
        
        b1.pack()
        space = tk.Label(master=windows, text="\n")
        space.pack()
##        windows.geometry("853x480")
##        windows.title('fogot password')
##        windows.mainloop()







##windows = tk.Tk()
##windows.geometry("853x480")
##
##
##forgotPassword2("himel@mit.edu",windows)
##
##windows.mainloop()

