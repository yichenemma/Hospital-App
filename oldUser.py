import datetime
import sqlite3
import sys
from sqlite3 import Error
from home2 import *


class oldUser:

    def __init__(self, email, password, window):
        self.window=window
        try:
            conn = sqlite3.connect('C:\\Users\\HimelSaha\\Documents\\PyCharm Projects\\Hospital app\\record.db')
            print(conn)
            print("::Database connected successfully::")
        except Error as e:
                print(e)
                print("::Failed to connect to the database::")
                sys.exit(1)


        self.email = email
        self.password = password


        c = conn.cursor()
        fetchedEntry = c.execute(f"SELECT * FROM record WHERE email = '{self.email}' and pass = '{self.password}'").fetchall()

        if len(fetchedEntry) == 0:
            # prompt error
            print("Wrong email and password combination, try again")
        else:
            print("Logged in successfully")
            window.withdraw()  # to close the window!!
            toplevel = tk.Toplevel(self.window)  # close the first window
            toplevel.geometry("853x480")
            homepage(email, toplevel)
        conn.commit()
        c.close()
