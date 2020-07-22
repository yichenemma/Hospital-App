import tkinter as tk
from tkinter import *
from login import *
from globalDict import *

class Record:
    
    def __init__(self, email, window):
        self.window = window
        self.email = email
        self.window.title('Medical Record')
        self.current_p = None

        space = tk.Label(self.window, text="\n")
        space.pack()
        
        greeting = tk.Label(self.window, text="View your medical record")
        greeting.pack()

        for pair in d:
            if self.email == pair:
                self.current_p = d[self.email]

                if not self.current_p.history.search == None:
                    
                    space = tk.Label(self.window, text="\n")
                    space.pack()

                    
                    mess = tk.Label(self.window, text=str(self.current_p.history.search))
                    mess.pack()
                    

        



'''

window = tk.Tk()
window.geometry("853x480")
Record(0,window)
window.mainloop()
'''
