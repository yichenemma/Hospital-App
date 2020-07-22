import datetime
import sqlite3
import sys
from sqlite3 import Error



try:
    conn = sqlite3.connect('C:\\Users\\HimelSaha\\Documents\\PyCharm Projects\\Hospital app\\record.db')
    print(conn)
    print("::Database connected successfully::")
except Error as e:
        print(e)
        print("::Failed to connect to the database::")
        sys.exit(1)


email = input("Enter your email address: ")
password = input("Enter your old password: ")

#entries = (first, middle, last, date_obj, int(age), int(num), email)   # tupple

c = conn.cursor()
fetchedEntry = c.execute(f"SELECT * FROM record WHERE email = '{email}' and pass = '{password}'")

if len(fetchedEntry.fetchall()) == 0:
    # prompt error
    print("no match")
else:
    #go to next phase
    #print(fetchedEntry.fetchall())

    newPass = input("Enter new password: ")
    c.execute(f"UPDATE record  SET pass = '{newPass}' WHERE email = '{email}' and pass = '{password}'")
    print("Password changed successfully")

conn.commit()
c.close()