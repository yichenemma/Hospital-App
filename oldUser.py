import datetime
import sqlite3
import sys
from sqlite3 import Error


class oldUser:

    def __init__(self, email, password):
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



        #entries = (first, middle, last, date_obj, int(age), int(num), email)   # tupple

        c = conn.cursor()
        fetchedEntry = c.execute(f"SELECT * FROM record WHERE email = '{self.email}' and pass = '{self.password}'")

        if len(fetchedEntry.fetchall()) == 0:
            # prompt error
            print("Wrong emil and password combination, try again")
        else:
            # go to next phase
            print("Logged in successfully")
        conn.commit()
        c.close()
