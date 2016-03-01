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
    

    if start=="e" :
        mlist = []
        keylist = []
        addlist=[]
        
        m=input("Message: ")
        key=input("Key: ")
        
        for x in m:
            mlist.append(associations.find(x))
        
        for x in key:
             keylist.append(associations.find(x))
        
        mlen=len(mlist)
        while mlen>0:
            keylist.append(keylist[len(mlist)-mlen])
            mlen=mlen-1
        ziplist=list(zip(keylist, mlist))
        for x in ziplist:
            addlist.append(x[0]+x[1])
        for x in addlist:
            if x<=len(associations):
                print(associations[x], end="")
            else:
                print(associations[x-len(associations)-1], end="")
    print()
    
    if start=="d" :
        mlist = []
        keylist = []
        addlist=[]
        
        m=input("Message: ")
        key=input("Key: ")
        
        for x in m:
            mlist.append(associations.find(x))
        
        for x in key:
             keylist.append(associations.find(x))
        
        mlen=len(mlist)
        while mlen>0:
            keylist.append(keylist[len(mlist)-mlen])
            mlen=mlen-1
        ziplist=list(zip(keylist, mlist))
        for x in ziplist:
            addlist.append(x[0]+x[1])
        for x in addlist:
            if x<=len(associations):
                print(associations[x], end="")
            else:
                print(associations[x-len(associations)-1], end="")
    print()
    
    
    


    if start!="e" and start!="d":
        print("Did not understand command, try again.")
        
    start=input("Enter e to encrypt, d to decrypt, or q to quit: ")


if start=="q" :
    print("Goodbye!")