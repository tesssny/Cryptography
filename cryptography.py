"""
cryptography.py
Author: Tess Snyder
Credit: Mary Feyrer

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"



start=input("Enter e to encrypt, d to decrypt, or q to quit: ")

while start!="q":
    mlist = []
    keylist = []


    if start=="e" :
        m=input("Message: ")
        key=input("Key: ")
        
        for x in m:
            mlist.append(associations.find(x))
        
        for x in key:
             keylist.append(associations.find(x))
    print(mlist)
    print(keylist)
    
    if start=="d" :
        m=input("Message: ")
        key=input("Key: ")
        print("decrypt")
    
    


    if start!="e" and start!="d":
        print("Did not understand command, try again.")
        
    start=input("Enter e to encrypt, d to decrypt, or q to quit: ")


if start=="q" :
    print("Goodbye!")