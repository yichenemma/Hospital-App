import tkinter as tk
from oldUser import *

# creat the window
window = tk.Tk()

#creat a lable, won't show up to the window until the nexet line
greeting = tk.Label(text="\nWelcome to the App!\n")
greeting.configure(font=("Lucida Console", 20, "bold"))
#height and with are measured in text unit

g2 = tk.Label(text = "Log-in\n")
g2.configure(font=("Lucida Console", 20,"bold"))
# add the label to the window
greeting.pack()
g2.pack()

email = tk.Label(text="E-Mail")
email.configure(font=("Lucida Console", 15))
email_entry = tk.Entry()
email_entry.insert(0, "example@xx.com")
email.pack()
email_entry.pack()



# password
pw = tk.Label(text="\npassword")
pw.configure(font=("Lucida Console", 15))
password = tk.Entry()
pw.pack()
password.pack()

def loginNext():
    email_input = email_entry.get()  # will go to database
    password_input = password.get()
    log = oldUser(email_input, password_input)

# for the medical condition
#mc = tk.Text()
#mc.pack()
space = tk.Label(text="\n")
space.pack()
send_b = tk.Button(master=window,text = "Log in", bg="purple", command=loginNext)
send_b.pack()
space = tk.Label(text="\n")
space.pack()

#sign-up option
space = tk.Label(text="\ndon't have an acocunt yet?")
space.pack()
send_b = tk.Button(master=window,text = "sign up")
send_b.pack()
space = tk.Label(text="\n")
space.pack()


window.geometry("853x480")
window.mainloop()
