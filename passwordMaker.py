import random as RAN
import string as STR
import sqlite3

#Connect SQL to the database
connection = sqlite3.Connection('database/database.db')

#add the SQL functionality
cursor = connection.cursor()


passLen = int(input("Length of password? "))
password = ""
software = input("What software is this for? ")
software.lower()

for i in range(passLen):
    ranChar = STR.printable[RAN.randint(0,99)]
    password += ranChar


cursor.execute(f"INSERT INTO userPassword (software, password) VALUES(?,?)", (software, password))
connection.commit()
print(f"\nPassword: {password} has been made and added to the database")