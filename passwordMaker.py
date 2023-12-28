import random as RAN # Random
import string as STR # An inport for all ascii chars
import sqlite3 # Adding SQL lite compatability

#Connect SQL to the database
connection = sqlite3.Connection('database/database.db')

#add the SQL functionality
cursor = connection.cursor()

# Getting the data for the password and its user software
passLen = int(input("Length of password? "))
password = ""
software = input("What software is this for? ")
software.lower()

# Looping the list for the password length
for i in range(passLen):
    ranChar = STR.printable[RAN.randint(0,99)]
    password += ranChar

# Adding all data to the sql database
cursor.execute("INSERT INTO userPassword (software, password) VALUES(?,?)", (software, password))
connection.commit()
print(f"\nPassword: {password} has been made and added to the database")