import datetime
import sqlite3
import sys
from sqlite3 import Error

class Database:

    def __init__(self, first, middle, last, date, num, question, ans, email, password):
        self.first = first
        self.middle = middle
        self.last = last
        self.date = date
        self.num = num
        self.question = question
        self.ans = ans
        self.email = email
        self.password = password


        #record(self.first, self.middle, self.last, self.date, self.age, self.num, self.email, self.password)

#def record(self, first, middle, last, date, age, num, email, password):
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



   # first = input("Enter your first name: ").strip()
   # middle = input("Enter your middle name: (type '/' if you don't have one) ").strip()
        if self.middle == '/':
            self.middle = None
   # last = input("Enter your last name: ").strip()
   # date = input("Enter your date of birth: (YYYY-MM-DD) ").strip()

        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()

   # age = input("Enter your age: ")
   # num = input("Enter your phone number: ")
   # email = input("Enter your email address: ").strip()
   # password = input("Choose your password: ").strip()

        entries = (self.first, self.middle, self.last, date_obj, int(self.age), int(self.num), self.question, self.ans, self.email, self.password)   # tupple

        c = conn.cursor()


        c.execute("INSERT INTO record(first, middle, last, bday, age, number, question, ans, email, pass) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", entries)
        print("::Data saved into database successfully::")
        conn.commit()
        c.close()