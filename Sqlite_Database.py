
import sqlite3
import os

# check if database exists 
if os.path.exists("mydb.db"):
    
    #Connect to and create new database
    database = sqlite3.connect("mydb.db")

    #create cursor to interact with database 
    cursor = database.cursor()
else:
    database = sqlite3.connect("mydb.db")

    cursor = database.cursor()

    #Values passed through here will execute. In this case, create a table with 2 values. 
    cursor.execute('''CREATE TABLE mydb
        (username text, password text)''')

    # Ask user if they would like to sign up or add in 
signOrLog = input('Press 1 if you want to sign up: \n Press 2 if you want to log in to an existing account: ')

# If the user inputs 1, ask them to create a username and password. 
if signOrLog == "1":
    username = input("Enter a username to add: ")
    password = input("Enter a password to add: ")

#Add user inputted values to table. The ? will be replaced with values inside the list. 
    cursor.execute("INSERT INTO mydb VALUES (?, ?)", [username, password])

#Commit to and close the database 
    database.commit()
    database.close()

    print("You have successfully created an account!")

# If the user enters 2 ask them to login in with their username and password.  
elif signOrLog == "2":
    username = input("Enter your username: ")
    password = input("Enter password: ")

#Check for username and password. If user input is incorrect let user know and if it is correct log user in.
    
#Select all elements saved from mydb table and compare to user input parameters from list. 
    
    cursor.execute("SELECT * FROM mydb WHERE username = ? and password = ?", [username, password])
    
#Returns the first row from the table and lets user know there is an error with login input.
    if cursor.fetchone() == None:
            print("Incorrect username or password")
    else:
            print("You are logged in!")
    
#Error checking
else:
    print("Please enter 1 or 2")

