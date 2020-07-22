import tkinter as tk
from forgotPassword2 import *


class forgotPassword1:
    def __init__(self, windows):
        # create the window
        #window = tk.Tk()
        self.windows = windows

        #create a lable, won't show up to the window until the nexet line
        title = tk.Label(master = windows,text = "\nReset password\n\n")
        title.configure(font=("Lucida Console", 20, "bold"))
        title.pack()


        email = tk.Label(master = windows,text="E-Mail")
        email.configure(font=("Lucida Console", 15))
        email.pack()
        space = tk.Label(master = windows,text="\n")
        space.pack()
        email_entry = tk.Entry(master = windows,)
        email_entry.insert(0,"example@xx.com")
        email_entry.pack()


        def nextPage2():
            windows.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.windows)  # close the first window
            toplevel.geometry("853x480")
            forgotPassword2(email_entry.get(), toplevel)
             

        space = tk.Label(master = windows,text="\n")
        space.pack()
        space = tk.Label(master = windows,text="\n")
        space.pack()
        b1 = tk.Button(master=windows,text = "Next", command=nextPage2)
        #windows.withdraw()
        b1.pack()

##        window = tk.Tk()
##        window.geometry("853x480")
##        window.mainloop()
