"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

start=input("Enter e to encrypt, d to decrypt, or q to quit: ")


if start=="e" :
    m=input("Message: ")
    key=input("Key: ")
    
    
if start=="d" :
    m=input("Message: ")
    key=input("Key: ")
    print("decrypt")
    
    
if start=="q" :
    print("Goodbye!")
    
    
if start!="q" and start!="e" and start!="d":
    print("Did not understand command, try again.")