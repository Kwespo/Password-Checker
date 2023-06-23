#imports sqlite3
import sqlite3

#Connect SQL to the database
connection = sqlite3.Connection('database\\UserData.db')

#add the SQL functionality
cursor = connection.cursor()

#makes a profile
def ProfileCreator():
    #Ask for Username
    while True: #provided it meets requirements it will pass onto next
      username = input("Enter your username, please: ")
      if len(username) >= 6 and len(username) <= 16: #larger or equal to 6 and smaller then and equal to 16.
        break
      else:
        print("Username must be at least 6 characters but smaller then 16")
    
    #Create an email address
    email = input("Enter your email, please: ") 
    
    while True:
      password = str(input("Enter your password, please: "))
      if len(password) >= 12 and len(password) <= 24: #larger or equal to 6 and smaller then and equal to 16.
        break
      else:
        print("Username must be at least 12 characters but smaller or equal to 24")
    
    cursor.execute(f"INSERT INTO UserData Values('{username}', '{email}', '{password}')")
    connection.commit()

#checks the inputted data to see if its an account, if it as itll sign you in.
def CheckData():
  #check username
  while True:
    cursor.execute(f"SELECT username FROM UserData")
    UserDetailResults_User = cursor.fetchone()

    C_username = input("Enter your username, please: ")
    if C_username == UserDetailResults_User[0]:
      break
    else:    
      print(f"No account matches the username: {C_username}")

  #gets the users details from the database
  cursor.execute(f"SELECT password FROM UserData WHERE username = '{C_username}'")
  UserDetailResults_Pass = cursor.fetchone()
  
  while True:
    C_password = input("Enter your password, please: ")
    if C_password == UserDetailResults_Pass[0]:
      print(f"Welcome {C_username}")
      break
    else:
      print("Wrong password. Please try again")


def Action():
  action = input("1 to make an account or 2 to sign in: ")
  if action == "1":
    ProfileCreator()
  elif action == "2":
    CheckData()
  else: 
    print("Please use a valid option")



if __name__ == "__main__":
  Action()

