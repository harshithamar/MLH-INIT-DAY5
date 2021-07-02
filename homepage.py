# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:36:21 2021

@author: bshpa
"""
import pclass as p
from store import store as store
from find_password import access
from password_generator import generator


#homepage for user to picks options

def main():
    print("Welcome to Password Manager, pick an option below: \na) Generate a password \nb) Get password for account\nc) Create new password")
    while True:
        user_choice=input("Enter your choice (a, b, or c): ")
        if user_choice=='a':
            #generate password
            #use password for a new account
            length=int(input("Please enter what length you'd like your password to be: "))
            pwrd=generator(length)
            print("Here is your new password: "+pwrd)
            break
        if user_choice=='b':
            #get password for an account
            access()
            break
        if user_choice=='c':
            #store password for a new account
            store()
            break
        else:
            print("Invalid input, please try again")

main()