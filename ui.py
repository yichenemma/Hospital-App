import tkinter as tk
from oldUser import *
from forgotPassword1 import *
from createAccount import *
from globalDict import *

class ui:
    def __init__(self, windows):
        # creat the window
        self.windows = windows
        #window = tk.Tk()

        try:
            conn = sqlite3.connect('C:\\Users\\HimelSaha\\Documents\\PyCharm Projects\\Hospital app\\record.db')
            print(conn)
            print("::Database connected successfully::")
        except Error as e:
                print(e)
                print("::Failed to connect to the database::")
                sys.exit(1)

        try:
            conn.execute('CREATE table record(id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, middle TEXT, last TEXT, '
                         'bday DATE, number NUMERIC, question TEXT, ans TEXT, email TEXT, pass TEXT)')
            print("::Table created successfully::", end="\n\n")
        except:
            print("::Table already exists::", end="\n\n")


        #creat a lable, won't show up to the window until the nexet line
        greeting = tk.Label(master = windows,text="\nWelcome to the App!\n")
        greeting.configure(font=("Lucida Console", 20, "bold"))
        #height and with are measured in text unit

        g2 = tk.Label(master = windows,text = "Log-in\n")
        g2.configure(font=("Lucida Console", 20,"bold"))
# add the label to the window
        greeting.pack()
        g2.pack()

        email = tk.Label(master = windows,text="E-Mail")
        email.configure(font=("Lucida Console", 15))
        email_entry = tk.Entry(master = windows)
        email_entry.insert(0, "example@xx.com")
        email.pack()
        email_entry.pack()

        # password
        pw = tk.Label(master = windows,text="\npassword")
        pw.configure(font=("Lucida Console", 15))
        password = tk.Entry(show="*")
        pw.pack()
        password.pack()

        def loginNext():
            email_input = email_entry.get()  # will go to database
            password_input = password.get()

            oldUser(email_input, password_input, windows)

        # for the medical condition
        #mc = tk.Text()
        #mc.pack()
        space = tk.Label(master = windows,text="\n")
        space.pack()
        send_b = tk.Button(master=windows,text = "Log in", bg="purple", fg="black", command=loginNext)
        send_b.pack()
        space = tk.Label(master = windows,text="\n")
        space.pack()

        def forgot():
            windows.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.windows)  # close the first window
            toplevel.geometry("853x480")
            forgotPassword1(toplevel)

        forget = tk.Button(master=windows, text = "Forgot Password?", command=forgot)
        forget.pack()

        def create():
            windows.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.windows)  # close the first window
            toplevel.geometry("853x480")
            createAccount(toplevel)

        #sign-up option
        space = tk.Label(text="\ndon't have an account yet?")
        space.pack()
        send_b = tk.Button(master=windows,text = "sign up", command=create)
        send_b.pack()
        space = tk.Label(master = windows,text="\n")
        space.pack()

##        windows = tk.Tk()
##        windows.geometry("853x480")
##        windows.mainloop()

