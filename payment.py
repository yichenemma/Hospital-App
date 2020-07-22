import tkinter as tk
from tkinter import *
from login import *
import webbrowser

class Payment:

    def __init__(self,window):
        self.window = window

        self.window.title("Payment")
        
        #balance = tk.Label(self.window, text='\nYour current balance is \n' + str(p1.balance) + '$')
        #balance.pack()

        space = tk.Label(self.window, text="\n")
        space.pack()

        def texas():
            webbrowser.open('https://www.texascapitalbank.com/')

        bank1 = tk.Button(self.window, text='Texas Capital Bank', command=texas)
        bank1.pack()

        space = tk.Label(self.window, text="\n")
        space.pack()

        def boa():
            webbrowser.open('https://www.bankofamerica.com/')

        bank2 = tk.Button(self.window, text='Bank Of America', command=boa)
        bank2.pack()

        space = tk.Label(self.window, text="\n")
        space.pack()

        def capital():
            webbrowser.open('https://www.capitalone.com/')

        bank3 = tk.Button(self.window, text='Capital One', command=capital)
        bank3.pack()

        space = tk.Label(self.window, text="\n")
        space.pack()

        def hsbc():
            webbrowser.open('https://www.us.hsbc.com/')

        bank4 = tk.Button(self.window, text='HSBC USA', command=hsbc)
        bank4.pack()

        space = tk.Label(self.window, text="\n")
        space.pack()

        def barclays():
            webbrowser.open('https://www.banking.barclaysus.com/index.html')

        bank5 = tk.Button(self.window, text='Barclays Bank', command=barclays)
        bank5.pack()

        space = tk.Label(self.window, text="\n")
        space.pack()
        





#window = tk.Tk()
        #window.geometry("853x480")
#Payment(window)

        #window.mainloop()
