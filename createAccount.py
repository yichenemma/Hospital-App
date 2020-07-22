import tkinter as tk
from tkinter import RIGHT, CENTER, TOP
from createAccount2 import *

class createAccount():
    def __init__(self, window):

        # create the window
        #window = tk.Tk()
        self.window = window


        title = tk.Label(master = window, text = "\nCreate new account\n")
        title.configure(font=("Lucida Console", 20, "bold"))
        title.pack()


        fname = tk.Label(master = window, text="First name")
        fname.configure(font=("Lucida Console", 15))
        fname.pack()
        fname_entry = tk.Entry(master = window)
        fname_entry.columnconfigure(4, pad=3)

        fname_entry.insert(0,"First name")
        fname_entry.pack()
        #space = tk.Label(text="\n")
        #space.pack()

        mname = tk.Label(master = window, text="Middle name")
        mname.configure(font=("Lucida Console", 15))
        fname_entry.columnconfigure(5, pad=3)
        mname.pack()
        mname_entry = tk.Entry(master = window)
        mname_entry.pack()
        mname_entry.insert(0,"Middle name")

        #space = tk.Label(text="\n")
        #space.pack()

        lname = tk.Label(master = window, text="Last name")
        lname.configure(font=("Lucida Console", 15))
        lname.pack()
        lname_entry = tk.Entry(master = window)
        lname_entry.insert(0,"Last name")
        lname_entry.pack()
        space = tk.Label(master = window, text="\n")
        space.pack()

        bday = tk.Label(master = window, text="Date of birth")
        bday.configure(font=("Lucida Console", 15))
        bday.pack()
        bday_entry = tk.Entry(master = window)
        bday_entry.insert(0,"YYYY-mm-dd")
        bday_entry.pack()
        space = tk.Label(master = window, text="\n")
        space.pack()

        phone = tk.Label(master = window, text="enter phone number")
        phone.configure(font=("Lucida Console", 15))
        phone.pack()
        phone_entry = tk.Entry(master = window)
        phone_entry.insert(0,"+514-xxx-xxxx")
        phone_entry.pack()
        space = tk.Label(master = window, text="\n")
        space.pack()

        def create2():
            window.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.window)  # close the first window
            toplevel.geometry("853x480")
            createAccount2(fname_entry.get(), mname_entry.get(), lname_entry.get(), bday_entry.get(), phone_entry.get(), toplevel)

        b1 = tk.Button(master=window,text = "Next", command=create2)
        b1.pack()


        #window.geometry("853x480")
        #window.mainloop()