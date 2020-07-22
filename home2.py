import tkinter as tk
from tkinter import *
from calender import *
from payment import *
from record import *

class homepage:
    def __init__(self, email, window):
        self.email = email
        self.window = window
        window.title('home')

        greeting = tk.Label(master=window, text='\nHome\n')
        greeting.pack()

        choose = tk.Label(master=window, text='Select your clinic/hospital\n')
        choose.pack()

        OPTIONS = [
        'General Hospital',
        'McGill Wellness Hub',
        'Royal Vicoria Hospital'
        ]

        variable = StringVar(window)
        variable.set(OPTIONS[0]) # default value

        w = OptionMenu(window, variable, *OPTIONS)

        w.pack()

        space1 = tk.Label(master=window, text="\n")
        space1.pack()



        '''not working'''
        def openCalender():
            greeting.destroy()
            choose.destroy()
            w.destroy()
            space1.destroy()
            schedule.destroy()
            space2.destroy()
            bill.destroy()
            record.destroy()
            space3.destroy()
            space4.destroy()
            
            #toplevel = tk.Toplevel(self.window)  # close the first window
            #toplevel.geometry("853x480")
            
            Calender(self.window)
            self.window.mainloop()
            print("cal")

        def openC():
            window.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.window)  # close the first window
            toplevel.geometry("853x480")
            Calender(toplevel)
      
            

        schedule = tk.Button(master=window, text = "Schedule an in person Appointment",command = openC)
        schedule.pack()

        space2 = tk.Label(master=window, text="\n")
        space2.pack()


        def openpay():
            window.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.window)  # close the first window
            toplevel.geometry("853x480")
            Payment(toplevel)
            
        
        bill = tk.Button(master=window, text = "Bill Payment",command=openpay)
        bill.pack()

        space3 = tk.Label(master=window, text="\n")
        space3.pack()


        def openR():
            window.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.window)  # close the first window
            toplevel.geometry("853x480")
            Record(self.email,toplevel)


        
        record = tk.Button(master=window, text = "Medical Record",command = openR)
        record.pack()

        space4 = tk.Label(master=window, text="\n")
        space4.pack()

'''
window=tk.Tk()
homepage("123@qq.com",window)
window.geometry("853x480")
window.mainloop()

'''
