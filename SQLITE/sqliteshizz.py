import sqlite3
import hashlib
import uuid
from datetime import date

conn = sqlite3.connect('example.db')

c = conn.cursor()



# Create table
#with conn:
#    c.execute('''CREATE TABLE users(
#        userid int, 
#        username text, 
#        date text, 
#        pwdSHA128 text)''')

#Insert a row of data

def logon():
    username = input("username")
    password = input("password")

def signin():
    username = "bob"
    password = "password"

    with conn:
        c.execute("INSERT INTO users VALUES ()")










# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()