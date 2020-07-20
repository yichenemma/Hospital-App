import tkinter as tk

# creat the window
window = tk.Tk()

#creat a lable, won't show up to the window until the nexet line
greeting = tk.Label(text = "\nWelcome to the App!\n")
greeting.configure(font=("Lucida Console", 20, "bold"))
#height and with are measured in text unit

g2 = tk.Label(text = "Log-in\n")
g2.configure(font=("Lucida Console", 20,"bold"))
# add the lable to the window
greeting.pack()
g2.pack()


email = tk.Label(text="E-Mail")
email.configure(font=("Lucida Console", 15))
email_entry = tk.Entry()
email_entry.insert(0,"example@xx.com")
email.pack()
email_entry.pack()

# password
pw = tk.Label(text="\npassword")
pw.configure(font=("Lucida Console", 15))
password = tk.Entry()
pw.pack()
password.pack()

# get the inpur from the user
#email_get = email_entry.get()
#print(email_get)

# for the medical condition
#mc = tk.Text()
#mc.pack()
space = tk.Label(text="\n")
space.pack()
send_b = tk.Button(master=window,text = "log in")
send_b.pack()
##############send_b.bind("<Return>", data_vali) ##### need to connect to the next page
space = tk.Label(text="\n")
space.pack()

forget = tk.Button(master=window, text = "Forgot Password?")
forget.pack()



#sign-up option
space = tk.Label(text="\ndon't have an account yet?")
space.pack()
send_b = tk.Button(master=window,text = "sign up")
send_b.pack()  ##########need to coonecty to the sign up
space = tk.Label(text="\n")
space.pack()


window.geometry("853x480")
# listsen for button clicks/keypresses event
window.mainloop()
