import sqlite3
import hashlib
import time
import os
import binascii


conn = sqlite3.connect('SQLITE/example.db')

c = conn.cursor()


# Create table
with conn:
    try:
        c.execute('''CREATE TABLE users(userId INTEGER, userName TEXT, time INTEGER, pwdSHA256 STRING, salt STRING)''')
    except Exception as e:
        pass


#Insert a row of data
def logon():
    username = input("username\n")
    password = input("password\n")
    

    
    #usr pwd


def signUp():
    username = input("username\n")
    password = input("password\n")
    
    currentTime = int(time.time())
    salt = os.urandom(16)

    with conn:
        lastIdx = c.execute(""" SELECT userid FROM users ORDER By userid DESC LIMIT 1""").fetchone()
        lastIdx = lastIdx[0] if lastIdx != None else -1
        insertion = (lastIdx + 1, username, currentTime, binascii.hexlify(hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), salt, 100_000)), binascii.hexlify(salt))

        print("INSERT INTO users (userId, userName, time, pwdSHA256, salt) VALUES (?, ?, ?, ?, ?)", insertion)
        c.execute("INSERT INTO users (userId, userName, time, pwdSHA256, salt) VALUES (?, ?, ?, ?, ?)", insertion)
        



signUp()







# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()