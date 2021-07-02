# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:48:41 2021

@author: bshpa
"""
import pclass as p
from password_generator import generator
from encryption import encryption
from encryption import decryption

#function that stores passwords
def store():
    f1=open("passwords.txt","a")
    platform=input("Please enter the platform name (e.g. Reddit, Instagram): ")
    email=input("Please enter the email id linked to this account: ")
    username=input("What is your username? ")
    password=input("What is your password? (if you wish to generate a password, please press g) ")
    if password=='g':
        p_len=int(input("Please enter what length you would like your password to be: "))
        password=generator(p_len)
        print("Your password is: "+str(password))
    encrypt_q=input("Would you like to encrypt your password? ")
    if encrypt_q=='Y':
        password=encryption(password)
        
    new_store=platform+" "+email+" "+username+" "+password+"\n"
    f1.write(new_store)
    print("Password stored!")
    f1.close()
