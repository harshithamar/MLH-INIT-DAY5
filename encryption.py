# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:47:53 2021

@author: bshpa
"""

#trying encryption
import numpy as np
import random

f1=open("encryption.txt","w")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()<>{}?+_"
    
x = uppercase_letters + lowercase_letters + digits + symbols
y = ''


index=list(np.random.randint(0,len(x),len(x)))
for i in range(len(x)-1):
    choice=x[index[i]]
    y=y+str(choice)
    del index[i]

f1.write(str(y)+"\n"+str(x))
f1.close()
    
def encryption(password):
    encrypted=''
    file1=open("encryption.txt","r")
    key=[]
    for line in file1:
        key=key+[line]
    scramble=str(key[0])
    normal=str(key[1])
    for i in range(len(password)):
        for j in range(len(normal)):
            if password[i]==normal[j]:
                encrypted=encrypted+str(scramble[j])
    file1.close()
    return encrypted
        
def decryption(decrypt):
    decrypted=''
    file2=open("encryption.txt","r")
    key=[]
    for line in file2:
        key=key+[line]
    scramble=str(key[0])
    normal=str(key[1])
    for i in range(len(decrypt)):
        for j in range(len(normal)):
            if decrypt[i]==scramble[j]:
                decrypted=decrypted+str(normal[j])
    file2.close()
    return decrypted


print(decryption('password'))
    


    
    
    
    