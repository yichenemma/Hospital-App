import tkinter as tk

# create the window
window = tk.Tk()

space = tk.Label(text="\n")
space.pack()

lbl = tk.Label(text="Select your priority")  # header label
lbl.configure(font=("Lucida Console", 15))
lbl.pack()

space = tk.Label(text="\n")
space.pack()
b1 = tk.Button(master=window,text = "Emergency")
b1.configure(font=("Lucida Console", 15))
b1.pack()


space = tk.Label(text="\n")
space.pack()


b2 = tk.Button(master=window,text = "Consultant")
b2.configure(font=("Lucida Console", 15))
b2.pack()

space = tk.Label(text="\n")
space.pack()
space = tk.Label(text="\n")
space.pack()

note = tk.Label(text = "\n\n*Note: The emergency service will place you in a higher priority \
but will charge you extra service fees")
note.configure(font=("Lucida Console", 10))
note.pack()
space = tk.Label(text="\n")
space.pack()

window.geometry("853x480")

window.mainloop()