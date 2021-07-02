# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:48:41 2021

@author: bshpa
"""
import pclass as p

#function that stores passwords
def store():
    f1=open("passwords.txt","a")
    platform=input("Please enter the platform name (e.g. Reddit, Instagram): ")
    email=input("Please enter the email id linked to this account: ")
    username=input("What is your username? ")
    password=input("What is your password? (if you wish to generate a password, please press g) ")
    #if password=='g':
        #generate password function
    #encrypt the password
    new_store=platform+" "+email+" "+username+" "+password+"\n"
    f1.write(new_store)
    print("Password stored!")
    f1.close()
