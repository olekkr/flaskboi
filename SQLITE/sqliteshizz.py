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
        print(e)
        pass


#Insert a row of data
def logon():
    username = input("username\n")
    password = input("password\n")
    
    # fails if input is mangled
    if not isClean(username):        
            print('failed due to unclean input')
            return False
    
    with conn:
        records = c.execute(f"SELECT * FROM users WHERE userName = '{username}'").fetchall()
        for user in records:
            print('user:', user)
            if binascii.hexlify(hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), binascii.unhexlify(user[4]), 100_000)).decode('utf-8')   ==   user[3].decode('utf-8'):
                return {"userId" : user[0], "userName" : user[1], "time" : user[2], "pwdSHA256" : user[3].decode('utf-8'), "salt" : user[4].decode('utf-8')}
        print('failed due to wrong password')
        return False

def isClean(input):
    illegal = ';\'\"\\' 
    for c in illegal:
        if c in input:
            return False
    return True

def signUp():
    username = input("username\n")
    password = input("password\n")
    
    currentTime = int(time.time())
    salt = os.urandom(16)

    with conn:
        lastIdx = c.execute(""" SELECT userid FROM users ORDER By userid DESC LIMIT 1""").fetchone()
        lastIdx = lastIdx[0] if lastIdx != None else -1
        insertion = (lastIdx + 1, username, currentTime, binascii.hexlify(hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), salt, 100_000)), binascii.hexlify(salt))
        
        c.execute("INSERT INTO users (userId, userName, time, pwdSHA256, salt) VALUES (?, ?, ?, ?, ?)", insertion)
        



signUp()
print(logon())






# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()